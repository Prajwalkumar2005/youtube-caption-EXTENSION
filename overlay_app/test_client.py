import asyncio
import websockets
import json
import sys
from bridge_server import load_or_create_config

async def test():
    cfg = load_or_create_config()
    token = sys.argv[1] if len(sys.argv) > 1 else cfg.get("auth_token", "")
    port = cfg.get("active_port", 48123)
    uri = f"ws://127.0.0.1:{port}/?token={token}"
    print(f"Connecting to {uri}...")
    async with websockets.connect(uri, additional_headers={"Origin": "chrome-extension://dummy"}) as ws:
        await ws.send(json.dumps({
            "type": "caption_update",
            "text": "Hello! The bridge is working perfectly!",
            "is_asr": False,
            "is_tag": False,
            "sent_at": 1000
        }))
        print("Test payload sent successfully.")

if __name__ == "__main__":
    asyncio.run(test())
