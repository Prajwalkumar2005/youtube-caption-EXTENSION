import unittest

def clamp_window_position(x, y, w, h, screen_w, screen_h):
    """Calculates clamped overlay geometry ensuring window stays on screen."""
    safe_w = min(max(320, w), max(600, screen_w - 40))
    safe_h = min(max(90, h), max(250, screen_h - 40))
    safe_x = x
    safe_y = y

    if safe_x < 0 or safe_x + 100 > screen_w:
        safe_x = max(20, (screen_w - safe_w) // 2)
    if safe_y < 0 or safe_y + 60 > screen_h:
        safe_y = 80

    return safe_x, safe_y, safe_w, safe_h

class TestScreenBoundary(unittest.TestCase):
    def test_normal_in_bounds(self):
        x, y, w, h = clamp_window_position(300, 80, 960, 160, 1920, 1080)
        self.assertEqual(x, 300)
        self.assertEqual(y, 80)
        self.assertEqual(w, 960)
        self.assertEqual(h, 160)

    def test_offscreen_left_clamped(self):
        x, y, w, h = clamp_window_position(-500, 80, 960, 160, 1920, 1080)
        # Should center on screen horizontally
        self.assertEqual(x, (1920 - 960) // 2)

    def test_offscreen_bottom_clamped(self):
        x, y, w, h = clamp_window_position(300, 1500, 960, 160, 1920, 1080)
        # Should reset vertical offset to safe top
        self.assertEqual(y, 80)

if __name__ == "__main__":
    unittest.main()
