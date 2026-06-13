CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name text,
    last_name text,
    email text UNIQUE
    );

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    price REAL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
    );