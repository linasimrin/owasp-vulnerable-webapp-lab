import sqlite3

def get_connection():
    conn = sqlite3.connect("shop.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL
    )
    """)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM users")

    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ("lina", "1234")
    )

    products = [
        ("Hello Kitty Tasche", 29.99),
        ("Hello Kitty Tasse", 14.99),
        ("Hello Kitty Hoodie", 49.99),
        ("Hello Kitty Schlüsselanhänger", 7.99)
    ]

    for product in products:
        conn.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            product
        )

    conn.commit()
    conn.close()