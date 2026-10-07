import sqlite3


class Inventory:
    """Stock levels kept in SQLite."""

    def __init__(self, path: str = ":memory:"):
        self.db = sqlite3.connect(path)
        self.db.execute("CREATE TABLE IF NOT EXISTS stock (sku TEXT PRIMARY KEY, name TEXT, qty INTEGER)")

    def put(self, sku: str, name: str, qty: int) -> None:
        self.db.execute(
            "INSERT INTO stock (sku, name, qty) VALUES (?, ?, ?) "
            "ON CONFLICT(sku) DO UPDATE SET name = excluded.name, qty = excluded.qty",
            (sku, name, qty),
        )
        self.db.commit()

    def available(self, sku: str) -> int:
        row = self.db.execute("SELECT qty FROM stock WHERE sku = ?", (sku,)).fetchone()
        return row[0] if row else 0

    def reserve(self, sku: str, qty: int) -> bool:
        if qty <= 0:
            return False
        cur = self.db.execute("UPDATE stock SET qty = qty - ? WHERE sku = ? AND qty >= ?", (qty, sku, qty))
        self.db.commit()
        return cur.rowcount == 1
