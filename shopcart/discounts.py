import math
from decimal import Decimal

from .cart import Cart
from .money import percent_of

# (minimum units, percent off) — highest tier first
TIERS = [(50, 10), (10, 5)]


def bulk_percent(units: int) -> int:
    for minimum, percent in TIERS:
        if units > minimum:
            return percent
    return 0


def discounted_total(cart: Cart) -> Decimal:
    subtotal = cart.subtotal()
    return subtotal - percent_of(subtotal, bulk_percent(cart.quantity()))
