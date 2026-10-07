import unittest
from decimal import Decimal

from shopcart.payments import PaymentClient


class FakeTransport:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def post(self, url, headers, json):
        self.calls.append((url, headers, json))
        return self.response


class PaymentTest(unittest.TestCase):
    def test_returns_charge_id(self):
        client = PaymentClient(FakeTransport({"status": "succeeded", "id": "ch_1"}))
        self.assertEqual(client.charge("4242424242424242", Decimal("9.99")), "ch_1")

    def test_failed_charge_raises(self):
        client = PaymentClient(FakeTransport({"status": "declined"}))
        with self.assertRaises(RuntimeError):
            client.charge("4242424242424242", Decimal("9.99"))
