from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (replace with your actual data source)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 20.99},
    {"id": 3, "name": "Product 3", "price": 30.99}
]

# Route to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a specific product by ID
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# Route to create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Route to update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product.update(data)
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# Route to delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return jsonify({'message': 'Product deleted'})

if __name__ == '__main__':
    app.run(debug=True)

