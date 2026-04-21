import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app.matcher import StreamingMatcher


class TestStreamScanner(unittest.TestCase):
    def setUp(self) -> None:
        self.matcher = StreamingMatcher()

    def test_positions_and_count(self) -> None:
        text = "x 100% y 3rd z"
        matches = self.matcher.find_matches(text)

        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].pattern, "100%")
        self.assertEqual(matches[1].pattern, "3rd")


if __name__ == "__main__":
    unittest.main()
