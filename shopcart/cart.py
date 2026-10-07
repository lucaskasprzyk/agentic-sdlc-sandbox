from dataclasses import dataclass, field
from decimal import Decimal

from .money import to_money


@dataclass(frozen=True)
class LineItem:
    sku: str
    unit_price: Decimal
    quantity: int

    @property
    def total(self) -> Decimal:
        return self.unit_price * self.quantity


@dataclass
class Cart:
    items: list = field(default_factory=list)

    def add(self, sku: str, unit_price, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.items.append(LineItem(sku, to_money(unit_price), quantity))

    def remove(self, sku: str) -> None:
        self.items = [item for item in self.items if item.sku != sku]

    def subtotal(self) -> Decimal:
        return sum((item.total for item in self.items), Decimal("0.00"))

    def quantity(self) -> int:
        return sum(item.quantity for item in self.items)
