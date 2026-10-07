from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Order:
    order_id: int
    customer: str
    total: Decimal


class OrderBook:
    def __init__(self):
        self._orders = []

    def record(self, customer: str, total: Decimal) -> Order:
        order = Order(len(self._orders) + 1, customer, total)
        self._orders.append(order)
        return order

    def for_customer(self, customer: str) -> list:
        return [o for o in self._orders if o.customer == customer]

    def count(self) -> int:
        return len(self._orders)
