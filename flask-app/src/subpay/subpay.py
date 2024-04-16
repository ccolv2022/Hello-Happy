from flask import Blueprint, request, jsonify, make_response
from src import db  # Ensure db module provides a connection to your database

# Create a blueprint named 'hellohappy'
subpay = Blueprint('subpay', __name__)

# List all subscriptions
@subpay.route('/subscriptions', methods=['GET'])
def list_subscriptions():
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM subscription")
    rows = cursor.fetchall()
    subscriptions = [dict(zip([key[0] for key in cursor.description], row)) for row in rows]
    return jsonify(subscriptions)

# Create a new subscription
@subpay.route('/subscriptions', methods=['POST'])
def create_subscription():
    data = request.get_json()
    cursor = db.get_db().cursor()
    try:
        cursor.execute("INSERT INTO subscription (subscriptionType, price, startDate, userId) VALUES (%s, %s, %s, %s)",
                       (data['subscriptionType'], data['price'], data['startDate'], data['userId']))
        db.get_db().commit()
        return jsonify({'message': 'Subscription created successfully'}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 400

# Retrieve a specific subscription
@subpay.route('/subscriptions/<int:subscription_id>', methods=['GET'])
def retrieve_subscription(subscription_id):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM subscription WHERE subscriptionId = %s", (subscription_id,))
    row = cursor.fetchone()
    if row:
        subscription = dict(zip([key[0] for key in cursor.description], row))
        return jsonify(subscription)
    else:
        return jsonify({'error': 'Subscription not found'}), 404

# Update a subscription
@subpay.route('/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    try:
        cursor.execute("UPDATE subscription SET subscriptionType = %s, price = %s, startDate = %s, userId = %s WHERE subscriptionId = %s",
                       (data['subscriptionType'], data['price'], data['startDate'], data['userId'], subscription_id))
        db.get_db().commit()
        return jsonify({'message': 'Subscription updated successfully'}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 400

# Cancel a subscription
@subpay.route('/subscriptions/<int:subscription_id>', methods=['DELETE'])
def delete_subscription(subscription_id):
    cursor = db.get_db().cursor()
    try:
        cursor.execute("DELETE FROM subscription WHERE subscriptionId = %s", (subscription_id,))
        db.get_db().commit()
        return jsonify({'message': 'Subscription deleted successfully'}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 400

# Process a new payment
@subpay.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    cursor = db.get_db().cursor()
    try:
        cursor.execute("INSERT INTO payment (amount, paymentDate, dueDate, userId) VALUES (%s, %s, %s, %s)",
                       (data['amount'], data['paymentDate'], data['dueDate'], data['userId']))
        db.get_db().commit()
        return jsonify({'message': 'Payment processed successfully'}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({'error': str(e)}), 400
