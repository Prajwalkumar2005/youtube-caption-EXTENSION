import unittest
import secrets
from bridge_server import BridgeServer

class TestTokenRotation(unittest.TestCase):
    def test_live_token_rotation(self):
        initial_token = secrets.token_hex(16)
        rotated_token = secrets.token_hex(16)
        server = BridgeServer({"auth_token": initial_token})

        self.assertEqual(server.auth_token, initial_token)
        server.auth_token = rotated_token
        self.assertEqual(server.auth_token, rotated_token)
        self.assertNotEqual(server.auth_token, initial_token)

if __name__ == "__main__":
    unittest.main()
