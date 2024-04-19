# HELLO-HAPPY MySQL + Flask Boilerplate Project

**Contributors:** Calli Colvin, Vrinda Rana, Kerissa Duliga, Lily Robinson, Jae Na Wray

**VIDEO LINK:** https://drive.google.com/drive/folders/1qmVlBV6lCRbS2za43gtcJSfRyDxLV_PY?usp=sharing 
## What's Hello Happy?

Hello Happy is a journal app that allows users to keep track of their daily activities and habits while keeping their therapist in the loop. Therapists can have administrative control over certain users, granting them access to observe the day-to-day elements that shape a patient's day. Users also have the option to use the app solely as a personal journal, without linking it to a therapist. The app offers input fields for users to log their daily activities, helping them identify patterns in their days. The files in this project repository create our hello-happy database and populate it with fake data.

## What's in This Repository?

Our repository includes the following components:

1. **Database**: A MySQL database schema that sets up the tables and relationships necessary for Hello Happy. The schema includes tables for users, entries, therapists, and more.

2. **Data Population Scripts**: Scripts to populate the database with fake data for testing and development purposes.

3. **Flask App**: A Python-based Flask web application that serves as the backend for Hello Happy. This folder includes routes and endpoints for retrieving user information, creating and updating journal entries, managing user-therapist relationships and  more.

4. **Docker Compose file**: A `docker-compose.yml` file to easily set up and run the application and its dependencies using Docker.

## How Can I Get Started?

To get started with the Hello Happy project, follow these steps:

1. **Clone the Repository**

2. **Create Secret Files**:
    - Create a file named `db_root_password.txt` in the `secrets/` folder and put inside it the root password for MySQL.
    - Create a file named `db_password.txt` in the `secrets/` folder and put inside it the password to use for the non-root user named `webapp`.

3. **Install Required Packages**: Install the required Python packages from the `requirements.txt` file.

4. **Create Docker Containers** 
`make sure Docker Desktop is installed on your machine`
    - In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
    - Build the images with `docker compose build`
    - Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`.  

**Stay happy!!**


