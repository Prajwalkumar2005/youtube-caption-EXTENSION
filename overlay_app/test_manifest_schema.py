import unittest
import json
import os

class TestManifestSchema(unittest.TestCase):
    def setUp(self):
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.manifest_path = os.path.join(root_dir, "extension", "manifest.json")
        with open(self.manifest_path, "r", encoding="utf-8") as f:
            self.manifest = json.load(f)

    def test_mv3_compliance(self):
        self.assertEqual(self.manifest.get("manifest_version"), 3)
        self.assertIn("version", self.manifest)
        self.assertIn("name", self.manifest)
        self.assertIn("description", self.manifest)

    def test_least_privilege_permissions(self):
        # Only storage and alarms allowed for MV3 least privilege
        permissions = set(self.manifest.get("permissions", []))
        self.assertEqual(permissions, {"storage", "alarms"})

    def test_host_permissions_bounded_to_youtube(self):
        host_perms = self.manifest.get("host_permissions", [])
        self.assertEqual(len(host_perms), 1)
        self.assertEqual(host_perms[0], "*://*.youtube.com/*")

    def test_icon_assets_exist(self):
        icons = self.manifest.get("icons", {})
        ext_dir = os.path.dirname(self.manifest_path)
        for size, rel_path in icons.items():
            full_path = os.path.join(ext_dir, rel_path)
            self.assertTrue(os.path.isfile(full_path), f"Icon {rel_path} does not exist on disk")

if __name__ == "__main__":
    unittest.main()
