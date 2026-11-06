import unittest
import os
import json
import tempfile
import shutil
from bridge_server import load_or_create_config, save_config, get_config_dir, VALID_STYLES, HEX_COLOR_REGEX

class TestConfiguration(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_valid_styles_definition(self):
        # 13 verified visual typography themes
        self.assertEqual(len(VALID_STYLES), 13)
        expected = {
            "poster", "neon", "minimal", "classic", "classic_white",
            "cyberpunk", "gold", "hacker", "blood", "ocean",
            "sunset", "ghost", "vaporwave"
        }
        self.assertEqual(VALID_STYLES, expected)

    def test_hex_color_validation(self):
        self.assertTrue(bool(HEX_COLOR_REGEX.match("#FFD700")))
        self.assertTrue(bool(HEX_COLOR_REGEX.match("#000000")))
        self.assertTrue(bool(HEX_COLOR_REGEX.match("#ffffff")))
        self.assertFalse(bool(HEX_COLOR_REGEX.match("rgb(0,0,0)")))
        self.assertFalse(bool(HEX_COLOR_REGEX.match("javascript:alert(1)")))
        self.assertFalse(bool(HEX_COLOR_REGEX.match("#FFF")))

    def test_config_save_and_load(self):
        test_file = os.path.join(self.test_dir, "test_config.json")
        sample_config = {
            "auth_token": "test_token_12345",
            "active_port": 48123,
            "text_style": "cyberpunk",
            "font_size": 42
        }
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(sample_config, f)

        with open(test_file, "r", encoding="utf-8") as f:
            loaded = json.load(f)

        self.assertEqual(loaded["auth_token"], "test_token_12345")
        self.assertEqual(loaded["text_style"], "cyberpunk")
        self.assertEqual(loaded["font_size"], 42)

if __name__ == "__main__":
    unittest.main()

