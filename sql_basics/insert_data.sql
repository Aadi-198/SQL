INSERT OR IGNORE INTO customers (id, first_name, last_name, email) 
VALUES 
    (1, 'John', 'Doe', 'john.doe@email.com'),
    (2, 'Jane', 'Smith', 'jane.smith@email.com'),
    (3, 'Alex', 'Jones', 'alex.jones@email.com');

INSERT INTO orders (item_name, price, customer_id)
VALUES
    ('Pro 3-Day Trial Upgrade', 0.00, 1),
    ('Premium Annual Subscription', 99.99, 1),
    ('Basic Monthly Plan', 9.99, 2),
    ('Developer API Access Key', 49.99, 3);