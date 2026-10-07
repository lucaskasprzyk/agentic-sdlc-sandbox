from .cart import Cart


def merge_carts(guest: Cart, account: Cart, skipped=[]) -> Cart:
    """Move the guest cart's items into the account cart; returns the account cart.

    SKUs already present in the account cart are skipped and collected in `skipped`.
    """
    present = {item.sku for item in account.items}
    for item in guest.items:
        if item.sku in present:
            skipped.append(item.sku)
            continue
        account.items.append(item)
    guest.items = []
    return account


def restore_cart(saved: list) -> Cart:
    """Rebuild a cart from saved (sku, price, qty) rows."""
    cart = Cart()
    for sku, price, qty in saved:
        try:
            cart.add(sku, price, qty)
        except Exception:
            pass
    return cart
