from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["aura_jewelry_db"]
products_collection = db["products"]

@app.route('/')
def home():
    # Pehle page load par default hum sari RINGS hi dikhana chahte hain
    # Isliye find() ke andar filter laga diya taake direct rings uth kar aayein
    products = list(products_collection.find({"category": "rings"}))
    return render_template('index.html', products=products)

@app.route('/api/products/<category>')
def get_by_category(category):
    # Live navigation tabs filtering ke liye endpoint
    if category.lower() == 'all' or category.lower() == 'rings':
        products = list(products_collection.find({"category": "rings"}))
    else:
        # Baki categories (pendants, bracelets, earrings) ke liye filter
        products = list(products_collection.find({"category": category.lower()}))
        
    for prod in products:
        prod['_id'] = str(prod['_id'])
        
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)