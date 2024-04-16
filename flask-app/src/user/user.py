from flask import Blueprint, request, jsonify, make_response
import json
from src import db

user = Blueprint('user', __name__)

# Get all users from the DB
@user.route('/user', methods=['GET'])
def get_user():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM user')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return make_response(jsonify(json_data), 200)

# Get detailed info for specific user
@user.route('/user/<int:userId>', methods=['GET'])
def get_users(userId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM user WHERE userId = %s', (userId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return make_response(jsonify(json_data), 200)

# Register new user
@user.route('/user', methods=['POST'])
def create_user():
    data = request.json
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO user (firstName, lastName, email, therapistId) VALUES (%s, %s, %s, %s)',
                   (data['firstName'], data['lastName'], data['email'], data['therapistId']))
    db.get_db().commit()
    return make_response(jsonify({"message": "User created successfully"}), 201)

# Update user details
@user.route('/user/<int:userId>', methods=['PUT'])
def update_user(userId):
    data = request.json
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE user SET firstName=%s, lastName=%s, email=%s WHERE userId=%s',
                   (data['firstName'], data['lastName'], data['email'], userId))
    db.get_db().commit()
    return make_response(jsonify({"message": "User updated successfully"}), 200)

# Delete a specific user
@user.route('/user/<int:userId>', methods=['DELETE'])
def delete_user(userId):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM user WHERE userId = %s', (userId,))
    db.get_db().commit()
    return make_response(jsonify({"message": "User deleted successfully"}), 200)

# Retrieve user settings for a specific user
@user.route('/user_settings/<int:userId>', methods=['GET'])
def get_user_settings(userId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM user_settings WHERE userId = %s', (userId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchone()  # Assuming there is only one settings row per user
    if theData:
        json_data = dict(zip(row_headers, theData))
    else:
        json_data = {'message': 'No settings found for the specified user.'}
    return make_response(jsonify(json_data), 200 if theData else 404)

# Update user settings for a specific user
@user.route('/user_settings/<int:userId>', methods=['PUT'])
def update_user_settings(userId):
    data = request.json
    cursor = db.get_db().cursor()
    update_statements = []
    update_values = []
    if 'notifications_on' in data:
        update_statements.append('notifications_on=%s')
        update_values.append(data['notifications_on'])
    if 'contacts_on' in data:
        update_statements.append('contacts_on=%s')
        update_values.append(data['contacts_on'])

    if not update_statements:
        return make_response(jsonify({'message': 'No settings provided to update.'}), 400)

    update_query = 'UPDATE user_settings SET ' + ', '.join(update_statements) + ' WHERE userId=%s'
    cursor.execute(update_query, update_values + [userId])
    db.get_db().commit()

    if cursor.rowcount == 0:
        return make_response(jsonify({'message': 'User settings not found.'}), 404)

    return make_response(jsonify({'message': 'User settings updated successfully.'}), 200)

# Retrieve users managed by a specific therapist
@user.route('/user/<int:therapistId>', methods=['GET'])
def get_user_by_therapist(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM user WHERE therapistId = %s', (therapistId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return make_response(jsonify(json_data), 200)

# Remove all users from a therapist's management
@user.route('/user/<int:therapistId>', methods=['DELETE'])
def remove_user_by_therapist(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM user WHERE therapistId = %s', (therapistId,))
    db.get_db().commit()
    affected_rows = cursor.rowcount
    if affected_rows > 0:
        return make_response(jsonify({'message': f'{affected_rows} user removed from therapist {therapistId}.'}), 200)
    else:
        return make_response(jsonify({'message': 'No user found for the specified therapist or no action taken.'}), 404)

# Retrieve all friend connections involving a specific user
@user.route('/friendlist/<int:userId>', methods=['GET'])
def get_friendlist(userId):
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT * FROM friendlist WHERE userId = %s OR friendId = %s', (userId, userId)
    )
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    friends = cursor.fetchall()
    for friend in friends:
        json_data.append(dict(zip(row_headers, friend)))
    return make_response(jsonify(json_data), 200)

# Remove all friend connections under a specific user
@user.route('/friendlist/<int:userId>', methods=['DELETE'])
def delete_all_friends(userId):
    cursor = db.get_db().cursor()
    cursor.execute(
        'DELETE FROM friendlist WHERE userId = %s OR friendId = %s', (userId, userId)
    )
    db.get_db().commit()
    return make_response(jsonify({'message': 'All friend connections removed for user {0}.'.format(userId)}), 200)

# Retrieve specific user-friend connection
@user.route('/friendlist/<int:userId>/<int:friendId>', methods=['GET'])
def get_specific_friend_connection(userId, friendId):
    cursor = db.get_db().cursor()
    cursor.execute(
        'SELECT * FROM friendlist WHERE (userId = %s AND friendId = %s) OR (userId = %s AND friendId = %s)',
        (userId, friendId, friendId, userId)
    )
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    friend = cursor.fetchone()
    if friend:
        json_data = dict(zip(row_headers, friend))
        return make_response(jsonify(json_data), 200)
    else:
        return make_response(jsonify({'message': 'No friend connection found.'}), 404)

# Remove specific friend connection
@user.route('/friendlist/<int:userId>/<int:friendId>', methods=['DELETE'])
def delete_specific_friend(userId, friendId):
    cursor = db.get_db().cursor()
    cursor.execute(
        'DELETE FROM friendlist WHERE (userId = %s AND friendId = %s) OR (userId = %s AND friendId = %s)',
        (userId, friendId, friendId, userId)
    )
    db.get_db().commit()
    return make_response(jsonify({'message': 'Friend connection removed.'}), 200)