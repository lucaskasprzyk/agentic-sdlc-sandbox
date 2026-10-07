from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def to_money(value) -> Decimal:
    """Parse a price given as str, int or Decimal into a 2-place Decimal."""
    if isinstance(value, float):
        raise TypeError("prices must not be floats; pass a str or Decimal")
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def percent_of(amount: Decimal, percent: int) -> Decimal:
    return (amount * Decimal(percent) / Decimal(100)).quantize(CENT, rounding=ROUND_HALF_UP)


def format_money(amount: Decimal, currency: str = "EUR") -> str:
    """Render an amount for receipts, e.g. `1,234.50 EUR`."""
    return f"{to_money(amount):,.2f} {currency}"
