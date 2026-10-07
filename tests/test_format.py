import unittest
from decimal import Decimal

from shopcart.money import format_money


class FormatTest(unittest.TestCase):
    def test_thousands_and_decimals(self):
        self.assertEqual(format_money(Decimal("1234.5")), "1,234.50 EUR")

    def test_currency_code(self):
        self.assertEqual(format_money(Decimal("0"), "PLN"), "0.00 PLN")

    def test_rounds_half_up(self):
        self.assertEqual(format_money(Decimal("2.345")), "2.35 EUR")
