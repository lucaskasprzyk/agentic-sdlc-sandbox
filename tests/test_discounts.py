import unittest
from decimal import Decimal

from shopcart.cart import Cart
from shopcart.discounts import bulk_percent, discounted_total


class DiscountTest(unittest.TestCase):
    def test_small_order_has_no_discount(self):
        self.assertEqual(bulk_percent(3), 0)

    def test_mid_tier(self):
        self.assertEqual(bulk_percent(20), 5)

    def test_top_tier(self):
        self.assertEqual(bulk_percent(80), 10)

    def test_discounted_total(self):
        cart = Cart()
        cart.add("A", "1.00", 20)
        self.assertEqual(discounted_total(cart), Decimal("19.00"))
