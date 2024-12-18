from flask import Flask, jsonify, request
import sqlite3
import os

app = Flask(__name__)

# Function to query database
def get_db_connection():
    # Get the absolute path to products.db in the backend folder
    db_path = os.path.join(os.path.dirname(__file__), 'products.db')
    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row  # To return results as dictionaries
    return connection

# Route to fetch all products or filter by category
@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')  # Optional filter
    if category:
        products = ("SELECT * FROM products WHERE category=?", (category,)) 
    else:
        products = ("SELECT * FROM products") 
    
    return jsonify([{'id': p[0], 'name': p[1], 'category': p[2], 'price': p[3]} for p in products])

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
