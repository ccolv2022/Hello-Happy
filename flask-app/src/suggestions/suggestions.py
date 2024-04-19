from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


suggestions = Blueprint('suggestions', __name__)

# Retrieve all suggestions data.
@suggestions.route('/suggestions', methods=['GET'])
def get_suggestions():
    cursor = db.get_db().cursor()
    cursor.execute('select *')

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get suggestions details from a specific  suggestion ID.
@suggestions.route('/suggestions/suggestionId/<sugId>', methods=['GET'])
def get_suggestion(sugId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM entry WHERE sugId = {0}'.format(sugId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get suggestions details from a specific  user ID.
@suggestions.route('/suggestions/<userId>', methods=['GET'])
def get_user_suggestion(userId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM entry WHERE sugId = {0}'.format(userId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get suggestions details from a specific therapist ID.
@suggestions.route('/suggestions/<therapistId>', methods=['GET'])
def get_therapist_suggestion(therapistId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM entry WHERE sugId = {0}'.format(therapistId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

 #Create a new suggestiom
@suggestions.route('/suggestions', methods=['POST'])
def add_new_suggestion():
    
    the_data = request.json
    current_app.logger.info(the_data)

    sugId = the_data['sugId']
    description = the_data['description']
    therapistId = the_data['therapistId']
    userId = the_data['userId']
    

    # Constructing the query
    query = '''
        INSERT INTO suggestions (sugId, description, therapistId, userId)
        VALUES (%s, %s, %s, %s)
    '''
    
    # Prepare data values tuple
    data = (sugId, description, therapistId, userId)

    cursor = db.get_db().cursor()
    cursor.execute(query,data)
    db.get_db().commit()
    
    return 'Success!'

#Update a suggestion from a suggestion ID
@suggestions.route('/suggestions/<sugId>', methods=['PUT'])
def update_suggestion(sugId):
    
    the_data = request.json
    current_app.logger.info(the_data)

    description = the_data['description']

    query = 'UPDATE suggestions SET description =' 
    query += description
    query += 'WHERE sugId ='
    query += sugId 
    
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#Delete a suggestion from a suggestion ID
@suggestions.route('/suggestions/<sugId>', methods=['DELETE'])
def delete_suggestion(sugId):
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'DELETE FROM suggestions WHERE sugId =' 
    query += sugId 

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'











































