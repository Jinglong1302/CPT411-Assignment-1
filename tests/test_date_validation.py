import unittest
from src.app.matcher import StreamingMatcher


class TestDateValidation(unittest.TestCase):
    def setUp(self):
        self.matcher = StreamingMatcher()

    def test_valid_date(self):
        matches = self.matcher.find_matches("12 March 2024")
        self.assertTrue(matches)
        self.assertEqual(matches[0].pattern, "12 March 2024")
        self.assertEqual(matches[0].category, "date")

    def test_day_too_long(self):
        matches = self.matcher.find_matches("123 March 2026")
        # should not produce a DATE category match
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_year_too_long(self):
        matches = self.matcher.find_matches("12 March 20245")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_april_31(self):
        matches = self.matcher.find_matches("31 April 2020")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_feb_29_leap(self):
        matches = self.matcher.find_matches("29 February 2020")
        self.assertTrue(matches)
        self.assertEqual(matches[0].category, "date")

    def test_feb_29_non_leap(self):
        matches = self.matcher.find_matches("29 February 2019")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_day_zero(self):
        matches = self.matcher.find_matches("0 March 2020")
        self.assertFalse(any(m.category == "date" for m in matches))

    def test_future_year_out_of_range(self):
        matches = self.matcher.find_matches("12 March 4040")
        self.assertFalse(any(m.category == "date" for m in matches))


if __name__ == "__main__":
    unittest.main()
