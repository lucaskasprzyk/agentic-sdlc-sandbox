import os
import tempfile
import unittest

from shopcart.inventory import Inventory


class InventoryTest(unittest.TestCase):
    def setUp(self):
        self.inv = Inventory()
        self.inv.put("A", "Apple", 5)

    def test_reserve_decrements(self):
        self.assertTrue(self.inv.reserve("A", 3))
        self.assertEqual(self.inv.available("A"), 2)

    def test_reserve_refuses_oversell(self):
        self.assertFalse(self.inv.reserve("A", 6))
        self.assertEqual(self.inv.available("A"), 5)

    def test_reserve_refuses_non_positive_quantity(self):
        self.assertFalse(self.inv.reserve("A", -3))
        self.assertFalse(self.inv.reserve("A", 0))
        self.assertEqual(self.inv.available("A"), 5)

    def test_writes_survive_reopening(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "stock.db")
            inv = Inventory(path)
            inv.put("A", "Apple", 5)
            self.assertTrue(inv.reserve("A", 3))
            inv.db.close()
            reopened = Inventory(path)
            self.assertEqual(reopened.available("A"), 2)
            reopened.db.close()

    def test_unknown_sku_has_no_stock(self):
        self.assertEqual(self.inv.available("Z"), 0)
