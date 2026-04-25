import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.app.matcher import StreamingMatcher


class TestAcceptCases(unittest.TestCase):
    def setUp(self) -> None:
        self.matcher = StreamingMatcher()

    def test_accept_examples(self) -> None:
        text = "3rd 100% 2017 16/09/2016 5 kg 2 g 7 ml 9 L 11 cm"
        matches = self.matcher.find_matches(text)
        patterns = [m.pattern for m in matches]

        self.assertIn("3rd", patterns)
        self.assertIn("100%", patterns)
        self.assertIn("2017", patterns)
        self.assertIn("16/09/2016", patterns)
        self.assertIn("5 kg", patterns)
        self.assertIn("2 g", patterns)
        self.assertIn("7 ml", patterns)
        self.assertIn("9 L", patterns)
        self.assertIn("11 cm", patterns)


if __name__ == "__main__":
    unittest.main()
