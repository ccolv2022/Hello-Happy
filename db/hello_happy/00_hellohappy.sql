CREATE DATABASE IF NOT EXISTS hello_happy;
USE hello_happy;


CREATE TABLE IF NOT EXISTS therapist (
   therapistId int PRIMARY KEY,
   firstName varchar(25),
   lastName varchar(25),
   email varchar(50) UNIQUE NOT NULL,
   phone varchar(50) UNIQUE NOT NULL
);


CREATE TABLE IF NOT EXISTS user (
   userId int PRIMARY KEY,
   firstName varchar(25),
   lastName varchar(25),
   email varchar(50) UNIQUE NOT NULL,
   therapistId int,
   CONSTRAINT userfk
         FOREIGN KEY (therapistId) references therapist(therapistId)
         ON UPDATE cascade ON DELETE restrict
);


CREATE TABLE IF NOT EXISTS friendlist(
   userId int,
   friendId int,
   primary key (userId, friendId),
   CONSTRAINT fk2
         FOREIGN KEY (friendId) references user (userId),
   CONSTRAINT fk3
         FOREIGN KEY (userId) references user (userId)
);


CREATE TABLE IF NOT EXISTS user_settings (
   userId int,
   notifications_on boolean DEFAULT false,
   contacts_on boolean DEFAULT false,
   CONSTRAINT fk4
           FOREIGN KEY (userId) references user(userId)
);


CREATE TABLE IF NOT EXISTS goals (
   goalId int PRIMARY KEY,
   completionStatus boolean DEFAULT false,
   description varchar(100),
   userId int,
   CONSTRAINT fk5
        FOREIGN KEY (userId) references user(userId)
);
CREATE TABLE IF NOT EXISTS meeting (
   meetingId int PRIMARY KEY,
   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
   topic varchar(200),
   isVirtual boolean DEFAULT false,
   therapistId int,
   userId int,
   CONSTRAINT meetingfk
       FOREIGN KEY (therapistId) references therapist (therapistId)
       ON UPDATE cascade ON DELETE cascade,
   CONSTRAINT fk6
       FOREIGN KEY (userId) references user (userId)
       ON UPDATE cascade ON DELETE cascade
);


CREATE TABLE IF NOT EXISTS suggestions (
   sugId int PRIMARY KEY,
   description text,
   therapistId int,
   userId int,
   CONSTRAINT suggestion_fk
            FOREIGN KEY (therapistId) references therapist (therapistId),
   CONSTRAINT fk7
            FOREIGN KEY (userId) references user (userId)
);


CREATE TABLE IF NOT EXISTS activities (
   activityId int AUTO_INCREMENT PRIMARY KEY,
   activityEntry varchar(255) NOT NULL
);


CREATE TABLE IF NOT EXISTS dayRating (
   ratingId int AUTO_INCREMENT PRIMARY KEY,
   ratingNum int NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS weatherLookup (
   weatherId int AUTO_INCREMENT PRIMARY KEY,
   weatherType varchar(15)
);


CREATE TABLE IF NOT EXISTS entry (
   entryId int PRIMARY KEY,
   timestamp DATETIME DEFAULT current_timestamp ON UPDATE current_timestamp,
   dayRating int NOT NULL,
   goodDay boolean DEFAULT true NOT NULL,
   moodRating int NOT NULL,
   peopleSeen int NOT NULL,
   meals text,
   ozWater int,
   hoursExercise int,
   exerciseIntensity int,
   hoursSleep int,
   people text,
   wakeUpTime DATETIME,
   sleepTime DATETIME,
   weather int,
   primaryLocation varchar(255),
   visibility boolean DEFAULT true,
   userId int,
   CONSTRAINT fk8
       FOREIGN KEY (userId) references user (userId)
       ON UPDATE cascade ON DELETE cascade,
   CONSTRAINT entryweatherfk
       FOREIGN KEY (weather) references  weatherLookup(weatherId)
       ON UPDATE cascade ON DELETE cascade
);


CREATE TABLE IF NOT EXISTS entry_activities (
   entryId int,
   activityId int,
   primary key (entryId, activityId),
   CONSTRAINT entryfk
       FOREIGN KEY (entryId) references entry (entryId)
       ON UPDATE cascade ON DELETE cascade,
   CONSTRAINT activityfk
       FOREIGN KEY (activityId) references activities (activityId)
       ON UPDATE cascade ON DELETE cascade
);


CREATE TABLE IF NOT EXISTS subscription (
   subscriptionId int PRIMARY KEY,
   subscriptionType varchar(50) NOT NULL,
   price DECIMAL(10, 2) NOT NULL,
   startDate DATE NOT NULL,
   userId int,
   CONSTRAINT fk9
       FOREIGN KEY (userId) references user (userId)
);


CREATE TABLE IF NOT EXISTS payment (
   paymentId int PRIMARY KEY,
   amount DECIMAL(10, 2) NOT NULL,
   paymentDate DATE NOT NULL,
   dueDate DATE NOT NULL,
   userId int,
   CONSTRAINT fk10
       FOREIGN KEY (userId) references user (userId)
);


/* 



-- INSERT statements


INSERT INTO therapist (therapistId, firstName, lastName, email, phone) VALUES
(1, 'John', 'Doe', 'john.doe@example.com', '123-456-7890'),
(2, 'Jane', 'Smith', 'jane.smith@example.com', '133-456-7891');


INSERT INTO user (userId, firstName, lastName, email, therapistId) VALUES
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', 1),
(2, 'Bob', 'Brown', 'bob.brown@example.com', 1),
(3, 'Charlie', 'Davis', 'charlie.davis@example.com', 2);


INSERT INTO friendlist (userId, friendId) VALUES
(1, 2),
(2, 1),
(2, 3),
(3, 2);


INSERT INTO user_settings (userId, notifications_on, contacts_on) VALUES
(1, true, true),
(2, false, true),
(3, true, false);


INSERT INTO goals (goalId, description, userId, completionStatus) VALUES
(1, 'Complete 5k run', 1, false),
(2, 'Read 10 books this year', 2, false),
(3, 'Learn to play guitar', 3, false);


INSERT INTO meeting (meetingId, topic, isVirtual, therapistId, userId) VALUES
(1, 'Initial Consultation', true, 1, 1),
(2, 'Follow-Up', false, 1, 2);


INSERT INTO suggestions (sugId, description, therapistId, userId) VALUES
(1, 'Try mindfulness meditation', 1, 1),
(2, 'Consider a regular exercise routine', 2, 2);


INSERT INTO activities (activityId, activityEntry) VALUES
(1, 'Running'),
(2, 'Reading'),
(3, 'Playing Guitar');


-- lookup table values (weather types for dropdown and rating increments)
INSERT INTO weatherLookup (weatherType)
VALUES ('cloudy'), ('sunny'), ('drizzly'), ('snow'), ('stormy');


INSERT INTO dayRating (ratingNum)
VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10);


INSERT INTO entry (entryId, dayRating, goodDay, moodRating, peopleSeen, meals, ozWater, hoursExercise, exerciseIntensity, hoursSleep, people, wakeUpTime, sleepTime, weather, primaryLocation, visibility, userId) VALUES
(1, 4, true, 7, 3, 'rice and spinach', 64, 1, 5, 8, 'Friends, Family', '2024-04-01 07:00:00', '2024-04-01 23:00:00', 1, 'Home', true, 1);


INSERT INTO entry_activities (entryId, activityId) VALUES
(1, 1),
(1, 2);


INSERT INTO subscription (subscriptionId, subscriptionType, price, startDate, userId) VALUES
(1, 'Monthly', 9.99, '2024-04-01', 1),
(2, 'Yearly', 99.99, '2024-04-01', 2);


INSERT INTO payment (paymentId, amount, paymentDate, dueDate, userId) VALUES
(1, 9.99, '2024-04-01', '2024-05-01', 1),
(2, 99.99, '2024-04-01', '2025-04-01', 2);


-- Persona CRUD Queries


-- Persona 1: Alex, the Independent User
-- Create (Daily Habit Tracking):
INSERT INTO entry (entryId, moodRating, hoursExercise, ozWater, userId)
VALUES (101, 8, 2, 64, 1);


-- Read (Mood and Activity Correlation Analysis):
SELECT moodRating, hoursExercise FROM entry WHERE userId = 1;


-- Update (Custom Privacy Settings for Entries):
UPDATE entry SET visibility = false WHERE entryId = 101 AND userId = 1;


-- Delete (Remove a specific entry):
DELETE FROM entry WHERE entryId = 102 AND userId = 1;


-- Persona 2: Laura, the Therapist
-- Create (Add a new suggestion):
INSERT INTO suggestions (sugId, description, therapistId, userId)
VALUES (201, 'Try mindfulness meditation', 2, 3);


-- Read (Patient Progress Monitoring):
SELECT * FROM entry WHERE userId IN (SELECT userId FROM user WHERE therapistId = 2);


-- Update (Modify an existing suggestion):
UPDATE suggestions SET description = 'Consider daily exercise' WHERE sugId = 201 AND therapistId = 2;


-- Delete (Remove a specific suggestion):
DELETE FROM suggestions WHERE sugId = 202 AND therapistId = 2;


-- Persona 3: Jeff, the Patient
-- Create (Log Daily Habits):
INSERT INTO entry (entryId, moodRating, hoursExercise, ozWater, userId)
VALUES (301, 6, 1, 48, 4);


-- Read (Professional Opinion on Activity Status):
SELECT * FROM entry WHERE userId = 4;


-- Update (Optional Privacy Entries):
UPDATE entry SET visibility = false WHERE entryId = 303 AND userId = 4;


-- Delete (Remove a specific entry):
DELETE FROM entry WHERE entryId = 304 AND userId = 4;


-- Persona 4: Caroline, the Independent User
-- Create (Log a new study session):
INSERT INTO entry (entryId, moodRating, hoursSleep, userId)
VALUES (401, 7, 6, 5);


-- Read (Study Session Optimization):
SELECT AVG(hoursSleep) AS AvgSleep, AVG(moodRating) AS AvgMood FROM entry WHERE userId = 5;


-- Update (Modify an existing study session entry):
UPDATE entry SET moodRating = 8, hoursSleep = 7 WHERE entryId = 402 AND userId = 5;


-- Delete (Physical Health Accountability):
DELETE FROM entry WHERE entryId = 403 AND userId = 5; */