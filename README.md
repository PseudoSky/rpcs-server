# RPCS API Documentation

This API has endpoints for User and Sensor values in the database. The API is hosted at http://128.2.20.131 with port 5000.

## User

###POST /api/user

###### Inserting a user 
For example, for a user with the following details -

- First Name - John
- Last Name - Doe
- Phone - 12345
- Address - 1234

You will type this into the terminal -

`curl -X POST http://128.2.20.131:5000/api/user -d "first=johnlast=doe&phone=12345&address=1234"'`

![Alt text](http://i.imgur.com/kn63zFK.png "Post User")

###GET /api/user/user_id

###### Retrieving a user by its user id
If you want to retrieve a user with the user id "user_id", just use the following command in the terminal -

`curl -X GET http://128.2.20.131:5000/api/user/user_id`

Here's how you would retrieve a user with user_id = 17, for example -

![Alt text](http://i.imgur.com/4k8fpsW.png "Get User")


###DELETE /api/user/user_id

###### Deleting a user by its user id
If you want to delete a user with the user id "user_id", just use the following command in the terminal -

`curl -X DELETE http://128.2.20.131:5000/api/user/user_id`

Here's how you would delete a user with user_id = 16, for example -

![Alt text](http://i.imgur.com/EYbuXhz.png "Delete User")

## Sensor

###POST /api/sensor

###### Adding a new sensor/Adding a value for an existing sensor

The commands to add a new sensor to the database or add a value for an existing sensor are the same.

For example, for a sensor with the following details -

- Sensor Name = Tricella
- User = 45 ( Note that you need the user ID specifcally, and other details are not sufficient)

To clarify the above, you would like to add a Tricella pillbox sensor for the user whose ID is 45.

To do so, you will type this into the terminal -

`curl -X POST http://128.2.20.131:5000/api/sensor -d "sensor_name=Tricella&uid=2"`

Note that the above assumes you do not want to add a value and simply add the sensor to the database.

In the event that you would like to add the sensor to the database along with a value OR add a value for an existing sensor (assume you already have a tricella sensor in the database), then the command would differ slightly. Say the value you are trying to add is 18.3

Then the command you would execute in your terminal would be:

`curl -X POST http://128.2.20.131:5000/api/sensor -d "sensor_name=Tricella&uid=2&value=18.3"`

###GET /api/sensor/sensor_name/user_id

###### Retrieving a sensor by its name and the user ID

If you want to retrieve the values of a sensor with name FITBIT belonging to user id 1, just use the following command in the terminal -

`curl -X GET http://128.2.20.131:5000/api/sensor/fitbit/1`