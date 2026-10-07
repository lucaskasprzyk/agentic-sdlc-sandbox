import unittest

from shopcart.inventory import Inventory


class SearchTest(unittest.TestCase):
    def test_finds_by_substring(self):
        inv = Inventory()
        inv.put("A", "Green Apple", 5)
        inv.put("B", "Banana", 2)
        self.assertEqual(inv.search("Apple"), [("A", "Green Apple", 5)])

    def test_match_is_case_sensitive(self):
        inv = Inventory()
        inv.put("A", "Green Apple", 5)
        self.assertEqual(inv.search("apple"), [])

    def test_no_match(self):
        self.assertEqual(Inventory().search("kiwi"), [])
