from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

try:
    
    MONGO_URI = "mongodb://127.0.0.1:27017/?directConnection=true"
    
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
  
    client.admin.command('ping')
    
    print(" DATABASE CONNECTION STATUS: SUCCESSFUL! ")
    
    
    db = client["aura_jewelry_db"]
    products_collection = db["products"]

except Exception as e:
    
    print(f" DATABASE CONNECTION FAILED! Error: {e}")
  
    products_collection = None



@app.route('/')
def home():
    if products_collection is None:
        return "Database connection issue! Please check terminal logs.", 500
    products = list(products_collection.find({"category": "rings"}))
    return render_template('index.html', products=products)

@app.route('/api/products/<category>')
def get_by_category(category):
    if products_collection is None:
        return jsonify({"error": "Database disconnected"}), 500

    if category.lower() == 'all' or category.lower() == 'rings':
        products = list(products_collection.find({"category": "rings"}))
    else:
        products = list(products_collection.find({"category": category.lower()}))
        
    for prod in products:
        prod['_id'] = str(prod['_id'])
        
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
