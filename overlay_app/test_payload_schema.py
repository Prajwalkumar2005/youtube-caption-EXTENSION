import unittest
from bridge_server import BridgeServer

class TestPayloadSchema(unittest.TestCase):
    def setUp(self):
        self.server = BridgeServer({"auth_token": "dummy"})

    def test_valid_caption_payload(self):
        valid = {"type": "caption_update", "text": "Valid subtitle text"}
        self.assertTrue(self.server.validate_payload(valid))

    def test_oversized_caption_clamping(self):
        oversized = {"type": "caption_update", "text": "A" * 1500}
        self.assertTrue(self.server.validate_payload(oversized))
        self.assertEqual(len(oversized["text"]), 1000)

    def test_invalid_types_rejected(self):
        self.assertFalse(self.server.validate_payload({"type": "unauthorized_op"}))
        self.assertFalse(self.server.validate_payload("not_a_dict"))
        self.assertFalse(self.server.validate_payload({}))

    def test_config_update_validation(self):
        self.assertTrue(self.server.validate_payload({"type": "config_update", "text_style": "poster"}))
        self.assertFalse(self.server.validate_payload({"type": "config_update", "text_style": "malicious"}))
        self.assertTrue(self.server.validate_payload({"type": "config_update", "font_size": 48}))
        self.assertFalse(self.server.validate_payload({"type": "config_update", "font_size": 1000}))

if __name__ == "__main__":
    unittest.main()
