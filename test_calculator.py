"""Task 9: automated regression tests."""
import unittest
from decimal import Decimal
from calculator import rate_per_litre, payout, validate

class CalculatorTests(unittest.TestCase):
    def test_standard_rate(self):
        self.assertEqual(rate_per_litre(3.5, 8.5), Decimal("30.00"))
    def test_above_standard(self):
        self.assertEqual(rate_per_litre(4.2, 8.7), Decimal("33.40"))
        self.assertEqual(payout(8.5, 4.2, 8.7), Decimal("283.90"))
    def test_below_standard(self):
        self.assertEqual(rate_per_litre(3.1, 8.3), Decimal("27.80"))
    def test_fat_min_and_max(self):
        validate(1, 2.0, 8.5)
        validate(1, 7.0, 8.5)
    def test_negative_litres(self):
        with self.assertRaises(ValueError):
            validate(-1, 3.5, 8.5)
    def test_invalid_fat(self):
        with self.assertRaises(ValueError):
            validate(1, 7.1, 8.5)

if __name__ == "__main__":
    unittest.main()
