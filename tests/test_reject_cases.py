import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app.matcher import StreamingMatcher


class TestRejectCases(unittest.TestCase):
    def setUp(self) -> None:
        self.matcher = StreamingMatcher()

    def test_reject_invalid_suffix_and_words(self) -> None:
        text = "4rx 22 Septembers abc 9 qqq"
        matches = self.matcher.find_matches(text)
        patterns = {m.pattern for m in matches}

        self.assertNotIn("4rx", patterns)
        self.assertNotIn("9 qqq", patterns)


if __name__ == "__main__":
    unittest.main()
