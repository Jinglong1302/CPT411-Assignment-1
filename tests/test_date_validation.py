import unittest
from src.app.matcher import StreamingMatcher


class TestDateValidation(unittest.TestCase):
    def setUp(self):
        self.matcher = StreamingMatcher()

    def test_valid_date_two_digit_day_month(self):
        matches = self.matcher.find_matches("12/03/2024")
        self.assertTrue(matches)
        self.assertEqual(matches[0].pattern, "12/03/2024")
        self.assertEqual(matches[0].category, "date")

    def test_valid_date_one_digit_day_month(self):
        matches = self.matcher.find_matches("1/2/2024")
        self.assertTrue(matches)
        self.assertEqual(matches[0].pattern, "1/2/2024")
        self.assertEqual(matches[0].category, "date")

    def test_day_too_long(self):
        matches = self.matcher.find_matches("123/03/2024")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_month_too_long(self):
        matches = self.matcher.find_matches("12/345/2024")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_year_too_short(self):
        matches = self.matcher.find_matches("12/03/123")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_year_too_long(self):
        matches = self.matcher.find_matches("12/03/20245")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_no_semantic_day_month_checks(self):
        matches = self.matcher.find_matches("99/99/1234")
        self.assertTrue(matches)
        self.assertEqual(matches[0].category, "date")


if __name__ == "__main__":
    unittest.main()
