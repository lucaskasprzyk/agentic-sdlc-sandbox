import unittest
from decimal import Decimal

from shopcart.cart import Cart


class CartTest(unittest.TestCase):
    def test_subtotal_sums_line_totals(self):
        cart = Cart()
        cart.add("A", "2.50", 2)
        cart.add("B", "1.25")
        self.assertEqual(cart.subtotal(), Decimal("6.25"))

    def test_empty_cart_is_zero(self):
        self.assertEqual(Cart().subtotal(), Decimal("0.00"))

    def test_rejects_non_positive_quantity(self):
        with self.assertRaises(ValueError):
            Cart().add("A", "1.00", 0)

    def test_remove_drops_sku(self):
        cart = Cart()
        cart.add("A", "1.00")
        cart.add("B", "2.00")
        cart.remove("A")
        self.assertEqual([i.sku for i in cart.items], ["B"])
