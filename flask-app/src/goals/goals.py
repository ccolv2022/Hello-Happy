from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db

goals = Blueprint('goals', __name__)


# Get all goals
@goals.route('/goals', methods=['GET'])
def get_goals():
    
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM goals')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Get specific goal from goalId
@goals.route('/goals/<goalId>', methods=['GET'])
def get_goal(goalId):

    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM goals WHERE goalId = %s', (goalId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Get goals made by a specific user
@goals.route('/goals/user/<userId>', methods=['GET'])
def get_user_goals(userId):

    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM goals WHERE userId = %s', (userId,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    return jsonify(json_data)


# Update specific goal
@goals.route('/goals/<goalId>', methods=['PUT'])
def update_goal(goalId):

    goal_info = request.json
    current_app.logger.info(goal_info)

    #extracting variables
    completionStatus = goal_info['completionStatus']
    description = goal_info['description']

    #constructing query
    query = 'UPDATE goals SET completionStatus = %s, description = %s WHERE goalId = %s'
    data = (completionStatus, description, goalId)
    current_app.logger.info(query)
    current_app.logger.info(data)

    #executing and committing the update statement 
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    return 'Goal updated!'


# Delete specific goal
@goals.route('/goals/<goalId>', methods=['DELETE'])
def delete_goal(goalId):

    cursor = db.get_db().cursor()
    cursor.execute('DELETE FROM goals WHERE goalId = %s', (goalId,))
    db.get_db().commit()

    return 'Goal deleted!'


# Create a new goal for a specific user
@goals.route('/goals/user/<userId>', methods=['POST'])
def add_goal(userId):
    
    goal_info = request.json
    current_app.logger.info(goal_info)

    #extracting variables
    completionStatus = goal_info['completionStatus']
    description = goal_info['description']

    #constructing query
    query = 'INSERT INTO goals (userId, completionStatus, description) VALUES (%s, %s, %s)'
    data = (userId, completionStatus, description)
    current_app.logger.info(query)
    current_app.logger.info(data)

    #executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    return 'Goal added!'