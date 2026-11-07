"""WebSocket Bridge Server for YouTube Desktop Lyrics Overlay.

Manages bidirectional communication between Google Chrome extension clients and the
local transparent Win32 Tkinter desktop overlay window. Enforces cryptographic pairing,
origin validation, sliding-window rate limiting, and frame bounds.
"""

import asyncio
import json
import secrets
import os
import sys
import re
import time
from typing import Dict, Any, Callable, Optional, Set, List, Tuple
import websockets
try:
    from websockets.asyncio.server import ServerConnection
except ImportError:
    ServerConnection = Any

DEFAULT_PORTS = [48123, 48124, 48125, 48126, 48127, 48128]
MAX_CONCURRENT_CLIENTS = 10
MAX_PAYLOAD_BYTES = 65536  # 64 KB per frame limit
MAX_MESSAGES_PER_SEC = 30   # DoS flood prevention

def generate_secure_token() -> str:
    """Generate a cryptographically secure 128-bit hex pairing token."""
    return secrets.token_hex(16)

def get_config_dir() -> str:
    """Resolve persistent configuration directory across script and frozen PyInstaller runtimes."""
    if getattr(sys, "frozen", False):
        appdata = os.environ.get("APPDATA") or os.path.expanduser("~")
        cfg_dir = os.path.join(appdata, "YTLyricsOverlay")
        os.makedirs(cfg_dir, exist_ok=True)
        return cfg_dir
    return os.path.dirname(os.path.abspath(__file__))

def get_config_path() -> str:
    return os.path.join(get_config_dir(), "config.json")

CONFIG_FILE = get_config_path()

VALID_STYLES = {
    "poster", "neon", "minimal", "classic", "classic_white",
    "cyberpunk", "gold", "hacker", "blood", "ocean",
    "sunset", "ghost", "vaporwave"
}
HEX_COLOR_REGEX = re.compile(r"^#[0-9a-fA-F]{6}$")

def load_or_create_config() -> Dict[str, Any]:
    default_config = {
        "auth_token": generate_secure_token(),
        "active_port": DEFAULT_PORTS[0],
        "always_on_top": True,
        "click_through": False,
        "lock_position": False,
        "show_visualizer": True,
        "bg_opacity": 0.85,
        "font_family": "Segoe UI",
        "font_size": 34,
        "font_color": "#FFFFFF",
        "highlight_color": "#FFD700",
        "window_x": 300,
        "window_y": 80,
        "window_w": 960,
        "window_h": 160,
        "text_style": "poster"
    }
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                default_config.update(data)
                # Ensure a valid token exists
                if not default_config.get("auth_token"):
                    default_config["auth_token"] = generate_secure_token()
        except Exception as e:
            print(f"[Config] Note: Loaded defaults due to: {e}")

    save_config(default_config)
    return default_config

def save_config(config: Dict[str, Any]):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)
    except Exception as e:
        print(f"[Config] Error saving config: {e}")

class BridgeServer:
    def __init__(self, config: Dict[str, Any], message_callback: Optional[Callable[[Dict[str, Any]], None]] = None):
        self.config = config
        self.auth_token = config.get("auth_token") or generate_secure_token()
        self.message_callback = message_callback
        self.active_clients: Set[Any] = set()
        self.client_rate_history: Dict[Any, list] = {}
        self.server = None
        self.bound_port = None

    async def validate_connection(self, websocket: ServerConnection) -> bool:
        # Enforce maximum concurrent connections to prevent connection flooding
        if len(self.active_clients) >= MAX_CONCURRENT_CLIENTS:
            print(f"[Security Rejected] Max concurrent connections ({MAX_CONCURRENT_CLIENTS}) reached.")
            return False

        origin = ""
        path = ""
        if hasattr(websocket, "request") and websocket.request:
            origin = websocket.request.headers.get("Origin", "")
            path = websocket.request.path
        elif hasattr(websocket, "request_headers"):
            origin = websocket.request_headers.get("Origin", "")
            path = getattr(websocket, "path", "")

        # Origin verification: must originate from a browser extension
        if not origin.startswith("chrome-extension://"):
            print(f"[Security Rejected] Invalid Origin: '{origin}'")
            return False

        # Query token verification using timing-safe comparison
        token = None
        if "?token=" in path:
            token = path.split("?token=")[-1].split("&")[0]

        if not token or not secrets.compare_digest(str(token), str(self.auth_token)):
            print(f"[Security Rejected] Token verification failed.")
            return False

        print(f"[Bridge] Verified connection from {origin}")
        return True

    def validate_payload(self, data: Dict[str, Any]) -> bool:
        if not isinstance(data, dict):
            return False
        msg_type = data.get("type")
        if not msg_type or not isinstance(msg_type, str):
            return False

        valid_types = {"caption_update", "play_state", "no_captions", "ping", "config_update"}
        if msg_type not in valid_types:
            return False

        if msg_type == "caption_update":
            if "text" not in data or not isinstance(data["text"], str):
                return False
            # Bound caption string to prevent memory exhaustion
            data["text"] = data["text"][:1000]

        elif msg_type == "config_update":
            if "text_style" in data:
                if not isinstance(data["text_style"], str) or data["text_style"] not in VALID_STYLES:
                    return False
            if "font_size" in data:
                if not isinstance(data["font_size"], (int, float)) or not (12 <= int(data["font_size"]) <= 80):
                    return False
                data["font_size"] = int(data["font_size"])
            if "highlight_color" in data:
                if not isinstance(data["highlight_color"], str) or not HEX_COLOR_REGEX.match(data["highlight_color"]):
                    return False

        elif msg_type == "play_state":
            if "is_playing" in data and not isinstance(data["is_playing"], bool):
                return False

        return True

    def is_rate_limited(self, websocket: ServerConnection) -> bool:
        now = time.time()
        history = self.client_rate_history.setdefault(websocket, [])
        # Prune timestamps older than 1 second
        self.client_rate_history[websocket] = [t for t in history if now - t < 1.0]
        if len(self.client_rate_history[websocket]) >= MAX_MESSAGES_PER_SEC:
            return True
        self.client_rate_history[websocket].append(now)
        return False

    async def handler(self, websocket: ServerConnection, path: str = ""):
        if not await self.validate_connection(websocket):
            await websocket.close(code=4001, reason="Unauthorized connection")
            return

        self.active_clients.add(websocket)
        self.client_rate_history[websocket] = []
        print(f"[Bridge] Extension client connected (Total: {len(self.active_clients)})")
        if self.message_callback:
            self.message_callback({"type": "client_connected"})

        try:
            async for message in websocket:
                if self.is_rate_limited(websocket):
                    print("[Bridge Security] Message dropped due to client rate limit")
                    continue

                try:
                    payload = json.loads(message)
                    if self.validate_payload(payload):
                        if payload.get("type") == "ping":
                            await websocket.send(json.dumps({"type": "pong"}))
                        elif self.message_callback:
                            self.message_callback(payload)
                    else:
                        print(f"[Bridge Security] Invalid payload schema discarded")
                except json.JSONDecodeError:
                    print("[Bridge Security] Malformed non-JSON data discarded")
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            if websocket in self.active_clients:
                self.active_clients.remove(websocket)
            if websocket in self.client_rate_history:
                del self.client_rate_history[websocket]
            print(f"[Bridge] Client disconnected (Remaining: {len(self.active_clients)})")
            if self.message_callback:
                self.message_callback({"type": "client_disconnected", "count": len(self.active_clients)})

    async def start(self):
        for port in DEFAULT_PORTS:
            try:
                self.server = await websockets.serve(
                    self.handler,
                    "127.0.0.1",
                    port,
                    max_size=MAX_PAYLOAD_BYTES
                )
                self.bound_port = port
                self.config["active_port"] = port
                save_config(self.config)
                print(f"[Bridge Server] Active and listening on 127.0.0.1:{port}")
                return port
            except OSError:
                print(f"[Bridge Server] Port {port} busy, testing next port...")

        raise RuntimeError("Failed to bind WebSocket server to any available port.")

    async def stop(self):
        if self.server:
            self.server.close()
            await self.server.wait_closed()
            print("[Bridge Server] Stopped cleanly.")

if __name__ == "__main__":
    cfg = load_or_create_config()
    def print_msg(msg):
        print("[Received]:", msg)

    async def main():
        server = BridgeServer(cfg, message_callback=print_msg)
        port = await server.start()
        print(f"Server online on port {port}. Token: {cfg['auth_token']}")
        await asyncio.Event().wait()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shutdown requested.")
