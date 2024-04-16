from flask import Blueprint, request, jsonify, make_response
import json
from src import db

therapists_blueprint = Blueprint('therapists', __name__)

# Get all therapists from the DB
@therapists_blueprint.route('/therapist', methods=['GET'])
def get_therapists():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM therapist')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return make_response(jsonify(json_data), 200)

# Get detailed info for a specific therapist
@therapists_blueprint.route('/therapist/<int:therapistId>', methods=['GET'])
def get_therapist(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM therapist WHERE therapistId = %s', (therapistId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return make_response(jsonify(json_data), 200)

# Register new therapist
@therapists_blueprint.route('/therapist', methods=['POST'])
def create_therapist():
    data = request.json
    cursor = db.get_db().cursor()
    cursor.execute('INSERT INTO therapist (firstName, lastName, email, phone) VALUES (%s, %s, %s, %s)',
                   (data['firstName'], data['lastName'], data['email'], data['phone']))
    db.get_db().commit()
    return make_response(jsonify({"message": "Therapist created successfully"}), 201)

# Update information for a specific therapist
@therapists_blueprint.route('/therapist/<int:therapistId>', methods=['PUT'])
def update_therapist(therapistId):
    data = request.json
    cursor = db.get_db().cursor()
    cursor.execute('UPDATE therapist SET firstName=%s, lastName=%s, email=%s, phone=%s WHERE therapistId=%s',
                   (data['firstName'], data['lastName'], data['email'], data['phone'], therapistId))
    db.get_db().commit()
    return make_response(jsonify({"message": "Therapist updated successfully"}), 200)

# Remove a specific therapist
@therapists_blueprint.route('/therapist/<int:therapistId>', methods=['DELETE'])
def delete_therapist(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM therapist WHERE therapistId = %s', (therapistId,))
    db.get_db().commit()
    return make_response(jsonify({"message": "Therapist deleted successfully"}), 200)

# Get a therapist's upcoming schedule
@therapists_blueprint.route('/therapist/<int:therapistId>/schedule', methods=['GET'])
def get_therapist_schedule(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute(
        '''
        SELECT m.meetingId, m.timestamp, m.topic, m.isVirtual, u.userId, u.firstName, u.lastName 
        FROM meeting m
        JOIN user u ON m.userId = u.userId
        WHERE m.therapistId = %s AND m.timestamp > NOW()
        ORDER BY m.timestamp ASC
        ''', (therapistId,)
    )
    row_headers = [x[0] for x in cursor.description]  # Get the columns names of the query
    json_data = []
    theData = cursor.fetchall()
    if theData:
        for row in theData:
            json_data.append(dict(zip(row_headers, row)))
        return make_response(jsonify(json_data), 200)
    else:
        return make_response(jsonify({'message': 'No upcoming schedule found for the specified therapist.'}), 404)
