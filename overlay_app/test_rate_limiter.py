import unittest
import time
from bridge_server import BridgeServer

class MockWebsocket:
    pass

class TestRateLimiter(unittest.TestCase):
    def test_sliding_window_rate_limiting(self):
        server = BridgeServer({"auth_token": "dummy"})
        ws = MockWebsocket()

        # The limit is 30 messages within 1.0s
        for i in range(30):
            self.assertFalse(server.is_rate_limited(ws), f"Request {i} should not be rate limited")

        # Request 31 should be rate limited
        self.assertTrue(server.is_rate_limited(ws), "Request 31 must be blocked by rate limiter")

        # After waiting > 1.0s, the sliding window resets
        time.sleep(1.05)
        self.assertFalse(server.is_rate_limited(ws), "Request after window reset must be accepted")

if __name__ == "__main__":
    unittest.main()
