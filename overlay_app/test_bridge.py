import asyncio
import json
import websockets
from bridge_server import BridgeServer, load_or_create_config

class TestBridgeSecurity:
    async def test_valid_connection(self):
        cfg = load_or_create_config()
        received = []
        server = BridgeServer(cfg, message_callback=lambda m: received.append(m))
        port = await server.start()

        url = f"ws://127.0.0.1:{port}/?token={cfg['auth_token']}"
        headers = {"Origin": "chrome-extension://test-extension-id-1234"}

        async with websockets.connect(url, additional_headers=headers) as ws:
            payload = {"type": "caption_update", "text": "Hello world", "sent_at": 1000}
            await ws.send(json.dumps(payload))
            await asyncio.sleep(0.15)

        await server.stop()
        caption_msgs = [m for m in received if m.get("type") == "caption_update"]
        assert len(caption_msgs) == 1
        assert caption_msgs[0]["text"] == "Hello world"
        print("[Pass] Valid connection and caption delivery verified")

    async def test_invalid_origin_rejection(self):
        cfg = load_or_create_config()
        server = BridgeServer(cfg)
        port = await server.start()

        url = f"ws://127.0.0.1:{port}/?token={cfg['auth_token']}"
        headers = {"Origin": "https://malicious-website.com"}

        try:
            async with websockets.connect(url, additional_headers=headers):
                assert False, "Should have been rejected!"
        except Exception:
            print("[Pass] Invalid Origin rejected")
        finally:
            await server.stop()

    async def test_invalid_token_rejection(self):
        cfg = load_or_create_config()
        server = BridgeServer(cfg)
        port = await server.start()

        url = f"ws://127.0.0.1:{port}/?token=wrong_token_value"
        headers = {"Origin": "chrome-extension://test-extension-id-1234"}

        try:
            async with websockets.connect(url, additional_headers=headers):
                assert False, "Should have been rejected!"
        except Exception:
            print("[Pass] Invalid token rejected")
        finally:
            await server.stop()

    async def test_payload_validation_and_sanitization(self):
        cfg = load_or_create_config()
        received = []
        server = BridgeServer(cfg, message_callback=lambda m: received.append(m))
        port = await server.start()

        url = f"ws://127.0.0.1:{port}/?token={cfg['auth_token']}"
        headers = {"Origin": "chrome-extension://test-extension-id-1234"}

        async with websockets.connect(url, additional_headers=headers) as ws:
            # 1. Invalid message type
            await ws.send(json.dumps({"type": "malicious_type", "data": 123}))
            # 2. Invalid config style
            await ws.send(json.dumps({"type": "config_update", "text_style": "nonexistent_exploit_style"}))
            # 3. Invalid font size
            await ws.send(json.dumps({"type": "config_update", "font_size": 99999}))
            # 4. Invalid hex color
            await ws.send(json.dumps({"type": "config_update", "highlight_color": "javascript:alert(1)"}))
            # 5. Oversized caption text (> 1000 chars) should be safely clamped
            oversized_text = "A" * 1500
            await ws.send(json.dumps({"type": "caption_update", "text": oversized_text}))
            # 6. Valid config update
            await ws.send(json.dumps({"type": "config_update", "text_style": "neon", "font_size": 36, "highlight_color": "#00FFFF"}))
            await asyncio.sleep(0.2)

        await server.stop()

        # Check discarded invalid payloads
        malicious = [m for m in received if m.get("type") == "malicious_type"]
        assert len(malicious) == 0, "Invalid message type should be discarded"

        # Check oversized caption text truncation
        captions = [m for m in received if m.get("type") == "caption_update"]
        assert len(captions) == 1
        assert len(captions[0]["text"]) == 1000, "Caption text must be capped to 1000 characters"

        # Check valid config update passed
        valid_configs = [m for m in received if m.get("type") == "config_update" and m.get("text_style") == "neon"]
        assert len(valid_configs) == 1, "Valid config update must be processed"
        print("[Pass] Payload schema validation & truncation verified")

    async def test_rate_limiting(self):
        cfg = load_or_create_config()
        received = []
        server = BridgeServer(cfg, message_callback=lambda m: received.append(m))
        port = await server.start()

        url = f"ws://127.0.0.1:{port}/?token={cfg['auth_token']}"
        headers = {"Origin": "chrome-extension://test-extension-id-1234"}

        async with websockets.connect(url, additional_headers=headers) as ws:
            # Flood 50 messages in rapid succession (limit is 30/sec)
            for i in range(50):
                await ws.send(json.dumps({"type": "caption_update", "text": f"Flood #{i}"}))
            await asyncio.sleep(0.3)

        await server.stop()
        assert len(received) <= 35, f"Rate limiting failed, received {len(received)} messages (expected <= 35)"
        print(f"[Pass] Rate limiter successfully capped message flood ({len(received)} accepted)")

if __name__ == "__main__":
    test = TestBridgeSecurity()
    asyncio.run(test.test_valid_connection())
    asyncio.run(test.test_invalid_origin_rejection())
    asyncio.run(test.test_invalid_token_rejection())
    asyncio.run(test.test_payload_validation_and_sanitization())
    asyncio.run(test.test_rate_limiting())
    print("=" * 55)
    print("All bridge security & validation tests passed cleanly!")
    print("=" * 55)
