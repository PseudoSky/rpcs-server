# RPCS API Documentation

This API has endpoints for User and Sensor values in the database. The API is hosted at http://128.2.20.131 with port 5000.

## User

###### Inserting a user 
For example, for a user with the following details -

- First Name - John
- Last Name - Doe
- Phone - 12345
- Address - 1234

You will type this into the terminal -

curl -X POST http://128.2.20.131:5000/api/user -d "first=johnlast=doe&phone=12345&address=1234"

![Alt text](http://i.imgur.com/kn63zFK.png "Post User")

###### Retrieving a user by its user id
If you want to retrieve a user with the user id "user_id", just use the following command in the terminal -
curl -X GET http://128.2.20.131:5000/api/user/user_id

Here's an example 




