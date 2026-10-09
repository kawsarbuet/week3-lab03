import unittest
from datetime import date

from fxsummary.aggregations import (
    MonthlyAverage,
    LargestSingleDayChange,
    MonthWithMostMovement,
)
from fxsummary.models import Record


class TestAggregations(unittest.TestCase):
    def setUp(self):
        self.records = [
            Record("2024-01-01", {"USD": 1.0, "EUR": 0.9}),
            Record("2024-01-02", {"USD": 1.1, "EUR": 0.95}),
            Record("2024-02-01", {"USD": 1.2, "EUR": 0.97}),
        ]

    def test_monthly_average(self):
        agg = MonthlyAverage()
        result = agg.compute(self.records)
        self.assertIn("2024-01", result)

    def test_largest_single_day_change(self):
        agg = LargestSingleDayChange()
        result = agg.compute(self.records)
        self.assertIn("USD", result)

    def test_month_with_most_movement(self):
        agg = MonthWithMostMovement()
        result = agg.compute(self.records)
        self.assertIn("USD", result)

