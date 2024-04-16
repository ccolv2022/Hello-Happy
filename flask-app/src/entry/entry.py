from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


entry = Blueprint('entry', __name__)

# Retrieve all entry data from the database
@entry.route('/entry', methods=['GET'])
def get_entries():
    cursor = db.get_db().cursor()

    cursor.execute('SELECT * FROM products')

    column_headers = [x[0] for x in cursor.description]

    json_data = []
    theData = cursor.fetchall()
 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get entry detail for user with particular userID
@entry.route('/entry/<userId>', methods=['GET'])
def get_user_entry(userId):
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM entry WHERE userId = {0}'.format(userId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Get entry detail for user with particular entryID
@entry.route('/entry/<entryId>', methods=['GET'])
def get_entry(entryId):
    cursor = db.get_db().cursor()
    cursor.execute('select * from entry where entryId = {0}'.format(entryId))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response 

# Update entry detail particular entryID
@entry.route('/entry/<entryId>', methods=['PUT'])
def update_entry(entryId):
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    dayRating = the_data['dayRating']
    goodDay = the_data['goodDay']
    moodRating = the_data['moodRating']
    peopleSeen = the_data['peopleSeen']
    meals = the_data['meals']
    ozWater = the_data['ozWater']
    hoursExercise = the_data['hoursExercise']
    exerciseIntensity = the_data['exerciseIntensity']
    people = the_data['people']
    wakeUpTime = the_data['wakeUpTime']
    sleepTime = the_data['sleepTime']
    weather = the_data['weather']
    primaryLocation = the_data['primaryLocation']
    visibility = the_data['visibility']

    query = '''
    UPDATE entry
    SET dayRating = %s, goodDay = %s, moodRating = %s, peopleSeen = %s,
        meals = %s, ozWater = %s, hoursExercise = %s, exerciseIntensity = %s,
        people = %s, wakeUpTime = %s, sleepTime = %s, weather = %s,
        primaryLocation = %s, visibility = %s
    WHERE entryId = %s
'''

    data = (
         dayRating, goodDay, moodRating, peopleSeen, meals, ozWater, hoursExercise,
         exerciseIntensity, people, wakeUpTime, sleepTime, weather, primaryLocation,
         visibility, entryId
        )

    current_app.logger.info(query, data)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    
    return 'Success!'

#Create new entry
@entry.route('/entry', methods=['POST'])
def add_new_entry():
    
    the_data = request.json
    current_app.logger.info(the_data)

    pk = the_data['dayRating']
    dayRating = the_data['dayRating']
    goodDay = the_data['goodDay']
    moodRating = the_data['moodRating']
    peopleSeen = the_data['peopleSeen']
    meals = the_data['meals']
    ozWater = the_data['ozWater']
    hoursExercise = the_data['hoursExercise']
    exerciseIntensity = the_data['exerciseIntensity']
    people = the_data['people']
    wakeUpTime = the_data['wakeUpTime']
    sleepTime = the_data['sleepTime']
    weather = the_data['weather']
    primaryLocation = the_data['primaryLocation']
    visibility = the_data['visibility']

    query = '''
        INSERT INTO entry (entryId, dayRating, goodDay, moodRating, peopleSeen, meals, ozWater, hoursExercise, 
                           exerciseIntensity, people, wakeUpTime, sleepTime, weather, primaryLocation, visibility)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    data = (pk, dayRating, goodDay, moodRating, peopleSeen, meals, ozWater, hoursExercise, 
            exerciseIntensity, people, wakeUpTime, sleepTime, weather, primaryLocation, visibility)
                                
    current_app.logger.info(query, data)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    
    return 'Success!'

#Delete a specific entry from an entry ID
@entry.route('/entry/<entryId>', methods=['DELETE'])
def delete_entry(entryId):
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'DELETE FROM entry WHERE entryId =' 
    query += entryId 

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#------------------DAY RATING-----------------------

#Retrieve all possible day ratings. 
@entry.route('/entry/dayRating/<int:dayRating>', methods=['GET'])
def get_dayRating():

    query = 'SELECT * FROM dayRating'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


#Retrieve day rating details from a specific ID. 
@entry.route('/entry/dayRating<ratingId>', methods=['GET'])
def get_adayRating(ratingId):

    query = 'SELECT * FROM dayRating WHERE ratingId =' + str(ratingId)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
   
    return jsonify(json_data)
   

#Add a new day rating.
@entry.route('/entry/dayRating', methods=['POST'])
def add_dayRating():
    
    the_data = request.json
    current_app.logger.info(the_data)

    num = the_data['ratingNum']
    
    query = 'INSERT INTO dayRating (ratingNum) VALUES ("'
    query += num + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#Update specific day rating number from a ratingId
@entry.route('/entry/dayRating<ratingId>', methods=['PUT'])
def update_dayRating(ratingId):

    the_data = request.json
    current_app.logger.info(the_data)

    num = the_data['rating']

    query = 'UPDATE dayRating SET ratingNum =' 
    query += num
    query += 'WHERE ratingId ='
    query += ratingId 
    
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#Delete specific day rating 
@entry.route('/entry/dayRating<ratingId>', methods=['DELETE'])
def delete_dayRating(ratingId):
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'DELETE FROM dayRating WHERE ratingId =' 
    query += ratingId 

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#------------------WEATHER LOOKUP-----------------------

#Retrieve all possible weather data. 
@entry.route('/entry/weather', methods=['GET'])
def get_weatherLookup():

    query = 'SELECT * FROM weatherLookup'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)


#Add a new weather option 
@entry.route('/entry/weather', methods=['POST'])
def add_weatherLookup():
    
    the_data = request.json
    current_app.logger.info(the_data)

    weatherType = the_data['weatherType']
    
    query = 'INSERT INTO weatherLookup (weatherType) VALUES ("'
    query += weatherType + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#Retrieve weatherLookup details from a specific ID. 
@entry.route('/entry/dayRating<weatherId>', methods=['GET'])
def get_dayRatings(weatherId):

    query = 'SELECT * FROM weatherLookup WHERE weatherId =' + str(weatherId)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
   
    return jsonify(json_data)


#Update specific weather type from a weatherId
@entry.route('/entry/weatherLookup<id>', methods=['PUT'])
def update_dayRatings(id):

    the_data = request.json
    current_app.logger.info(the_data)

    type = the_data['weatherType']

     # Constructing the query
    query = '''
        UPDATE weatherLookup
        SET weatherType = %s
        WHERE weatherId = %s
    '''

    # Prepare data values tuple
    data = (type, id)
    
    current_app.logger.info(query, data)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    
    return 'Success!'

#Delete specific weather lookup
@entry.route('/entry/weatherLookup<id>', methods=['DELETE'])
def delete_weatherLookup(ID):
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'DELETE FROM weatherLookup WHERE weatherId =' 
    query += id 

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#-----------------------ACTIVITIES----------------------------

# Retrieve details of all activities 
@entry.route('/entry/activity', methods=['GET'])
def get_activities():

    query = 'SELECT * FROM activities'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
    return jsonify(json_data)

# Create a new activity
@entry.route('/entry/activity', methods=['POST'])
def add_activities():
    
    the_data = request.json
    current_app.logger.info(the_data)

    activityId = the_data['activityId']
    activityEntry = the_data['activityEntry']

    query = 'INSERT INTO activities (activityId, activityEntry) VALUES ("'
    query += activityId + ','
    query += activityEntry + ')'
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

#Retrieve activity details from a specific ID. 
@entry.route('/entry/dayRating<id>', methods=['GET'])
def get_activity(id):

    query = 'SELECT * FROM activites WHERE activityId =' + str(id)
    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    column_headers = [x[0] for x in cursor.description]
    json_data = []
    the_data = cursor.fetchall()
    for row in the_data:
        json_data.append(dict(zip(column_headers, row)))
   
    return jsonify(json_data)

#Update specific activity type from an id
@entry.route('/entry/activity<id>', methods=['PUT'])
def update_activity(id):

    the_data = request.json
    current_app.logger.info(the_data)

    entry = the_data['entry']

     # Constructing the query
    query = '''
        UPDATE activities
        SET activityEntry = %s
        WHERE activityId = %s
    '''

    # Prepare data values tuple
    data= (entry, id)

    current_app.logger.info(query, data)

    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()
    
    return 'Success!'

#Delete specific activity from an id
@entry.route('/entry/activity<id>', methods=['DELETE'])
def delete_activity(ID):
    
    the_data = request.json
    current_app.logger.info(the_data)

    query = 'DELETE FROM activities WHERE activityId =' 
    query += id 

    current_app.logger.info(query)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'







 















































