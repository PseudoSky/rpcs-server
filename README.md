# RPCS API Documentation

This API has endpoints for User and Sensor values in the database. The API is hosted at http://128.2.20.131 with port 5000.

## User

###### Inserting a user 
For example, for a user with the following details -
First Name - John
Last Name - Doe
Phone - 12345
Address - 1234
You will tpye this into the terminal -
curl -X POST http://128.2.20.131:5000/api/user -d "first=johnlast=doe&phone=12345&address=1234"

![Alt text](http://i.imgur.com/fPw2b3b.pngg "Post User")

###### Retrieving a user by its user id
Just type this into the terminal -
curl -X GET http://127.0.0.1:5000/api/user/"user id"

Here's an example 




