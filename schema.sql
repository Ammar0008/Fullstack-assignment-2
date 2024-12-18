CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);


INSERT INTO products (name, category, price) VALUES 
('Laptop', 'Electronics', 799.99),
('Headphones', 'Electronics', 49.99),
('Fiction Book', 'Books', 14.99),
('Non-Fiction Book', 'Books', 19.99),
('Cotton Shirt', 'Textiles', 29.99);
