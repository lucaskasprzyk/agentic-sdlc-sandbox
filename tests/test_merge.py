import unittest

from shopcart.cart import Cart
from shopcart.merge import merge_carts, restore_cart


class MergeTest(unittest.TestCase):
    def test_moves_new_items(self):
        guest, account = Cart(), Cart()
        guest.add("A", "1.00")
        account.add("B", "2.00")
        merged = merge_carts(guest, account)
        self.assertEqual(sorted(i.sku for i in merged.items), ["A", "B"])
        self.assertEqual(guest.items, [])

    def test_restore(self):
        cart = restore_cart([("A", "1.00", 2)])
        self.assertEqual(cart.quantity(), 2)
