import unittest

class TestWin32Styles(unittest.TestCase):
    # Constants from main_overlay.py
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x00080000
    WS_EX_TRANSPARENT = 0x00000020
    WS_EX_NOACTIVATE = 0x08000000
    WS_EX_TOOLWINDOW = 0x00000080
    LWA_ALPHA = 0x00000002

    def test_bitmask_operations(self):
        base_style = self.WS_EX_TOOLWINDOW | self.WS_EX_NOACTIVATE
        self.assertTrue(base_style & self.WS_EX_TOOLWINDOW)
        self.assertTrue(base_style & self.WS_EX_NOACTIVATE)
        self.assertFalse(base_style & self.WS_EX_TRANSPARENT)

        # Toggle click-through ON
        click_through_style = base_style | self.WS_EX_TRANSPARENT
        self.assertTrue(click_through_style & self.WS_EX_TRANSPARENT)

        # Toggle click-through OFF
        restored_style = click_through_style & ~self.WS_EX_TRANSPARENT
        self.assertFalse(restored_style & self.WS_EX_TRANSPARENT)
        self.assertEqual(restored_style, base_style)

    def test_non_overlapping_bitmasks(self):
        masks = [
            self.WS_EX_LAYERED,
            self.WS_EX_TRANSPARENT,
            self.WS_EX_NOACTIVATE,
            self.WS_EX_TOOLWINDOW,
            self.LWA_ALPHA
        ]
        # Verify no two masks share common bits
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                self.assertEqual(masks[i] & masks[j], 0)

if __name__ == "__main__":
    unittest.main()
