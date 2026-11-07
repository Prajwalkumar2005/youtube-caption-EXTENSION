import unittest

def find_caption_binary_search(captions, time_ms):
    """Python reference implementation of the content.js binary search sync."""
    low = 0
    high = len(captions) - 1
    while low <= high:
        mid = (low + high) // 2
        cap = captions[mid]
        if time_ms >= cap["startMs"] and time_ms <= cap["endMs"]:
            return cap
        elif time_ms < cap["startMs"]:
            high = mid - 1
        else:
            low = mid + 1
    return None

class TestCaptionSearch(unittest.TestCase):
    def setUp(self):
        self.captions = [
            {"startMs": 1000, "endMs": 3000, "text": "First lyric segment"},
            {"startMs": 3500, "endMs": 5500, "text": "Second lyric segment"},
            {"startMs": 6000, "endMs": 8500, "text": "Third lyric segment"}
        ]

    def test_exact_start_and_end_matches(self):
        res1 = find_caption_binary_search(self.captions, 1000)
        self.assertIsNotNone(res1)
        self.assertEqual(res1["text"], "First lyric segment")

        res2 = find_caption_binary_search(self.captions, 3000)
        self.assertIsNotNone(res2)
        self.assertEqual(res2["text"], "First lyric segment")

    def test_midpoint_matches(self):
        res = find_caption_binary_search(self.captions, 4000)
        self.assertIsNotNone(res)
        self.assertEqual(res["text"], "Second lyric segment")

    def test_inter_lyric_gaps(self):
        # 3200ms is between segment 1 (ends 3000) and segment 2 (starts 3500)
        res = find_caption_binary_search(self.captions, 3200)
        self.assertIsNone(res)

    def test_out_of_bounds(self):
        self.assertIsNone(find_caption_binary_search(self.captions, 500))
        self.assertIsNone(find_caption_binary_search(self.captions, 12000))

    def test_empty_captions(self):
        self.assertIsNone(find_caption_binary_search([], 2000))

if __name__ == "__main__":
    unittest.main()
