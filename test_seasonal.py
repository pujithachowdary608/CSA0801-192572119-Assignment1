"""Task 12: tests for original and seasonal rates."""
import unittest
from decimal import Decimal
from seasonal_calculator import rate_per_litre, ten_day_payment

class SeasonalTests(unittest.TestCase):
    def test_original_base_rate(self):
        self.assertEqual(rate_per_litre(3.5, 8.5, 2), Decimal("30.00"))
    def test_seasonal_base_rate(self):
        self.assertEqual(rate_per_litre(3.5, 8.5, 4), Decimal("32.00"))
    def test_bonus_threshold_not_reached(self):
        total, volume, bonus = ten_day_payment([(100, 3.5, 8.5)], 4)
        self.assertEqual(bonus, Decimal("0.00"))
    def test_bonus_threshold_exceeded(self):
        total, volume, bonus = ten_day_payment([(501, 3.5, 8.5)], 4)
        self.assertEqual(bonus, Decimal("250.50"))

if __name__ == "__main__":
    unittest.main()
