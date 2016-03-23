#!flask/bin/python
from flask import Flask, jsonify
from db_definitions import *
import flask.ext.restful as rest
from pony import orm

class Settings:
    DB_PROVIDER = "sqlite"
    DB_NAME = "inventory.db"
    DEBUG = True

app = Flask(__name__)
api = rest.Api(app)
app.config.from_object(Settings)

#retrieve a user
@app.route('/api/user/get/<int:user_id>', methods=['GET'])
def get_user_byID(user_id):    
    try:
        return jsonify({'first': User[user_id].first,
                'last' : User[user_id].last,
                'phone': User[user_id].phone,
                'address': User[user_id].address})
    except:
        return "404 Error"

#insert a user
@app.route('/api/user/post/<string:first>/<string:last>/<int:phone>/<string:address>')
def make_user(first, last, phone, address):
    new_id = db.insert("User", first=first, 
                               last=last, 
                               phone=phone, 
                               address=address, 
                               classType="User", 
        returning='id')
    return jsonify({'new_id' : new_id})

#delete a user
@app.route('/api/user/delete/<int:user_id>')
def delete_user_byID(user_id):
    try:
        User[user_id].delete()
        return "User deleted"
    except:
        return "404 Error"

@app.route('/api/sensor/get/<string:sensor_name>', methods=['GET'])
def get_sensor(sensor_name):
    # Need to get values from sensor and return it
    try:
        return jsonify({'Name': Sensor[sensor_name].name}) 
    except:
        return "404 Error"

@app.route('/api/sensor/add/<string:sensor_name>')
def add_sensor(sensor_name):
    sensor_name = db.insert("Sensor", name=sensor_name, classType="Sensor", 
        returning=sensor_name)
    return jsonify({'Sensor Name' : sensor_name})

@app.route('/api/sensor/del/<string:sensor_name>')
def del_sensor(sensor_name):
    try:
        Sensor[sensor_name].delete()
        return "Sensor "+sensor_name+" deleted"
    except:
        # Sensor with this name does not exist
        return "404 Error"

if __name__ == '__main__':
    app.wsgi_app = orm.db_session(app.wsgi_app)
    app.run(debug=True)

