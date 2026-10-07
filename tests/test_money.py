import unittest
from decimal import Decimal

from shopcart.money import percent_of, to_money


class MoneyTest(unittest.TestCase):
    def test_rounds_half_up(self):
        self.assertEqual(to_money("1.005"), Decimal("1.01"))

    def test_refuses_float(self):
        with self.assertRaises(TypeError):
            to_money(1.5)

    def test_percent_of(self):
        self.assertEqual(percent_of(Decimal("19.99"), 10), Decimal("2.00"))
