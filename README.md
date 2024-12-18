E-commerce Sales Chatbot
This project demonstrates the development of an interactive e-commerce sales chatbot using Flask (Python) for the backend and Alpine.js for the frontend. The chatbot allows users to interact with an e-commerce platform, search for products, and view details.

Table of Contents
Project Description
Features
Technologies Used
Setup Instructions
API Endpoints
Database Setup
Project Structure
Project Description
This project is a sales chatbot built for an e-commerce platform, focusing on a specific product category (e.g., books, electronics, textiles). It allows users to search for products, view details, and filter products by category. The backend is powered by Flask, and the frontend uses Alpine.js for a lightweight and reactive user experience.

Features
Product Search: Search for products by name or category.
Product Listing: View a list of products with names, categories, and prices.
Responsive UI: Built to work seamlessly on desktop, tablet, and mobile devices.
Simple Database: SQLite database storing mock product data.
API Integration: The frontend communicates with the backend via RESTful APIs to fetch product data.
Technologies Used
Frontend:

Alpine.js (JavaScript framework for reactive UI)
HTML5, CSS3
Backend:

Flask (Python web framework)
SQLite (Database)
Setup Instructions
1. Clone the repository
bash
Copy code
git clone https://github.com/your-username/ecommerce-sales-chatbot.git
cd ecommerce-sales-chatbot
2. Install the necessary dependencies
Frontend:
No additional setup is required for Alpine.js (included in index.html).
Backend:
Install Python dependencies:
bash
Copy code
pip install -r requirements.txt
If requirements.txt is missing, you can manually install Flask and SQLite:
bash
Copy code
pip install flask sqlite3
3. Set up the database
Make sure the products.db file exists in the backend folder. If not, you can create it using SQLite:
bash
Copy code
sqlite3 products.db
Create the products table and insert mock data:
sql
Copy code
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);

INSERT INTO products (name, category, price) VALUES
    ('Book 1', 'Books', 9.99),
    ('Laptop', 'Electronics', 999.99),
    ('T-Shirt', 'Clothing', 19.99);
API Endpoints
GET /products: Fetch all products or filter by category.
Example: http://127.0.0.1:5000/products
Example with category filter: http://127.0.0.1:5000/products?category=Books
Project Structure
graphql
Copy code
ecommerce-sales-chatbot/
│
├── backend/
│   ├── app.py                # Flask backend code
│   ├── products.db           # SQLite database with mock data
│   └── requirements.txt      # List of Python dependencies
│
├── index.html                # Frontend HTML file with Alpine.js
├── style.css                 # Custom CSS for styling
└── README.md                 # Project documentation
License
This project is licensed under the MIT License.

Author
Mohammad Ammar
