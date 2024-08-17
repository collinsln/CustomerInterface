from flask import request, jsonify
from app import app, db
from models import Customer

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


# Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'preference': customer.preference
    } for customer in customers])

# Get a specific customer by ID
@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify({
        'id': customer.id,
        'name': customer.name,
        'email': customer.email,
        'phone_number': customer.phone_number,
        'preference': customer.preference
    })

# Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(
        name=data['name'],
        email=data['email'],
        phone_number=data['phone_number'],
        preference=data['preference']
    )
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({'message': 'Customer created successfully!'}), 201

# Update an existing customer
@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    data = request.get_json()
    customer.name = data['name']
    customer.email = data['email']
    customer.phone_number = data['phone_number']
    customer.preference = data['preference']
    db.session.commit()
    return jsonify({'message': 'Customer updated successfully!'})

# Delete a customer
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({'message': 'Customer deleted successfully!'})
