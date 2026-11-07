import unittest
import asyncio
import json
import websockets
from bridge_server import BridgeServer, load_or_create_config

class TestBridgeIntegration(unittest.TestCase):
    def test_end_to_end_loopback(self):
        async def run_scenario():
            cfg = load_or_create_config()
            received_messages = []

            def on_msg(payload):
                received_messages.append(payload)

            server = BridgeServer(cfg, message_callback=on_msg)
            port = await server.start()

            url = f"ws://127.0.0.1:{port}/?token={cfg['auth_token']}"
            headers = {"Origin": "chrome-extension://production-test-client"}

            async with websockets.connect(url, additional_headers=headers) as ws:
                # 1. Send ping
                await ws.send(json.dumps({"type": "ping", "sent_at": 1000}))
                # 2. Send caption
                await ws.send(json.dumps({
                    "type": "caption_update",
                    "text": "Synchronized lyrics stream test",
                    "is_asr": True,
                    "is_tag": False,
                    "sent_at": 1050
                }))
                await asyncio.sleep(0.15)

            await server.stop()

            # Verify connection lifecycle and caption reception
            captions = [m for m in received_messages if m.get("type") == "caption_update"]
            self.assertEqual(len(captions), 1)
            self.assertEqual(captions[0]["text"], "Synchronized lyrics stream test")

        asyncio.run(run_scenario())

if __name__ == "__main__":
    unittest.main()
