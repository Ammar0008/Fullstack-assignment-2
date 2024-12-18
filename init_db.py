import sqlite3
import os 

# Connect to SQLite database (creates 'products.db' if it doesn't exist)
connection = sqlite3.connect('products.db')
cursor = connection.cursor()

# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
''')

# Insert sample data
products = [
    ('Laptop', 'Electronics', 799.99),
    ('Headphones', 'Electronics', 49.99),
    ('Fiction Book', 'Books', 14.99),
    ('Non-Fiction Book', 'Books', 19.99),
    ('Cotton Shirt', 'Textiles', 29.99),
    ('Jeans', 'Textiles', 49.99),
    ('Smartphone', 'Electronics', 599.99)
]

cursor.executemany('INSERT INTO products (name, category, price) VALUES (?, ?, ?)', products)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Database 'products.db' created successfully with sample data!")
