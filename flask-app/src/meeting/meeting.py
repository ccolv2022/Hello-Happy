from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


meeting = Blueprint('meeting', __name__)


# Get all meetings and details
@meeting.route('/meeting', methods=['GET'])
def get_meetings():
   
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM meeting')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Get a specific meeting
@meeting.route('/meeting/<meetingId>', methods=['GET'])
def get_meeting(meetingId):
   
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM meeting WHERE meetingId = %s', (meetingId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Create a new meeting
@meeting.route('/meeting', methods=['POST'])
def create_meeting():
    meeting_info = request.json
    current_app.logger.info(meeting_info)

    # Extracting variables
    meetingId = meeting_info['meetingId']
    timestamp = meeting_info['timestamp']
    topic = meeting_info['topic']
    isVirtual = meeting_info['isVirtual']
    therapistId = meeting_info['therapistId']
    userId = meeting_info['userId']

    # Constructing the query
    query = 'INSERT INTO meeting (meetingId, timestamp, topic, isVirtual, therapistId, userId) VALUES (%s, %s, %s, %s, %s, %s)'
    data = (meetingId, timestamp, topic, isVirtual, therapistId, userId)
    current_app.logger.info(query)
    current_app.logger.info(data)

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query, data)  # Correctly passing the data tuple
    db.get_db().commit()

    return 'Meeting created!'


@meeting.route('/meeting/<meetingId>', methods=['PUT'])
def update_meeting(meetingId):
    meeting_info = request.json
    current_app.logger.info(meeting_info)

    # Extracting variables
    timestamp = meeting_info['timestamp']
    topic = meeting_info['topic']
    isVirtual = meeting_info['isVirtual']
    therapistId = meeting_info['therapistId']
    userId = meeting_info['userId']

    # Constructing query
    query = 'UPDATE meeting SET timestamp = %s, topic = %s, isVirtual = %s, therapistId = %s, userId = %s WHERE meetingId = %s'
    data = (timestamp, topic, isVirtual, therapistId, userId, meetingId)
    current_app.logger.info(query)
    current_app.logger.info(data)

    # Executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    return jsonify({'message': 'Meeting updated!'}), 200



# Get meetings scheduled for specific user
@meeting.route('/meeting/user/<userId>', methods=['GET'])
def get_user_meetings(userId):

    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM meetings WHERE userId = %s', (userId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Get meetings scheduled by specific therapist
@meeting.route('/meeting/therapist/<therapistId>', methods=['GET'])
def get_therapist_meetings(therapistId):

    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM meetings WHERE therapistId = %s', (therapistId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Delete specific meeting
@meeting.route('/meeting/<meetingId>', methods=['DELETE'])
def delete_meeting(meetingId):

    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM meeting WHERE meetingId = %s', (meetingId,))
    db.get_db().commit()

    return 'Meeting deleted!'