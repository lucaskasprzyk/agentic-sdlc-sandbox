import unittest
from decimal import Decimal

from shopcart.orders import OrderBook


class PageTest(unittest.TestCase):
    def test_page_size_is_respected(self):
        book = OrderBook()
        for _ in range(25):
            book.record("ann", Decimal("1.00"))
        self.assertEqual(len(book.page("ann", 1, size=10)), 10)

    def test_other_customers_excluded(self):
        book = OrderBook()
        book.record("ann", Decimal("1.00"))
        self.assertEqual(book.page("bob", 1), [])
