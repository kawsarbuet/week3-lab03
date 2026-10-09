import unittest
from fxsummary.models import Record


class TestRecord(unittest.TestCase):
    def test_valid_record(self):
        rec = Record("2024-01-15", {"USD": 1.23, "EUR": 0.91})
        self.assertEqual(rec.date.year, 2024)
        self.assertIn("USD", rec.rates)

    def test_invalid_rate_map(self):
        with self.assertRaises(ValueError):
            Record("2024-01-15", "not-a-dict")


