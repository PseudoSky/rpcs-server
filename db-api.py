#!flask/bin/python
from flask import Flask, jsonify,request
from db_definitions import *
from decimal import Decimal
import flask.ext.restful as rest
from pony import orm
import datetime

from flask_restful import reqparse,abort



class Settings:
    DB_PROVIDER = "sqlite"
    DB_NAME = "inventory.db"
    DEBUG = True

app = Flask(__name__)
api = rest.Api(app)
app.config.from_object(Settings)


def abort_if_null(keys,obj):
    # print(obj)
    errors=[]
    for key in keys:
        print(key not in obj or obj[key] is None)
        if (key not in obj) or obj[key] is None:
            errors.append("{}  doesn't exist in object".format(key))

    return errors


#retrieve a user
@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_byID(user_id):    
    try:
        return jsonify({'first': User[user_id].first,
                'last' : User[user_id].last,
                'phone': User[user_id].phone,
                'address': User[user_id].address})
    except:
        return "404 Error"

# curl -X POST http://127.0.0.1:5000/api/user -d "first=sky&last=frank&phone=707&address=1234"
@app.route('/api/user', methods=['POST'])
def mk_user():
    parser = reqparse.RequestParser()
    parser.add_argument('first', type=str, help='Rate to charge for this resource')
    parser.add_argument('last', type=str, help='Rate to charge for this resource')
    parser.add_argument('phone', type=str, help='Rate to charge for this resource')
    parser.add_argument('address', type=str, help='Rate to charge for this resource')

    args = parser.parse_args()
    errors = abort_if_null( ['first','last','phone','address'] , args)
    if len(errors)>0: return jsonify({'errors':errors})
    new_id = db.insert("User", first=args['first'], last=args['last'], phone=args['phone'], address=args['address'], classType="User", returning='id')
    return jsonify({'id':new_id})


#delete a user
@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user_byID(user_id):
    try:
        User[user_id].delete()
        return "User deleted"
    except:
        return "No user found with that ID"

#delete all users
@app.route('/api/user/drop',methods=['GET'])
def delete_all_users():
    try:
        delete(u for u in User)
        return "All users deleted"
    except:
        return "No users found"

@app.route('/api/sensor/<sensor_name>', methods=['GET'])
def get_sensor_ByName(sensor_name):
    # Need to get values from sensor and return it
    try:
        s = Sensor.get(name=sensor_name)
        # consider converting into a list
        return jsonify(Values=s.values)   # returning a set of values
    except:
        return "404 Error"

@app.route('/api/sensor', methods=['POST'])
def update_sensor_ByName():
    try:
        parser = reqparse.RequestParser()
        parser.add_argument('sensor_name', type=str, help='Rate to charge for this resource')
        parser.add_argument('uid', type=int, help='Rate to charge for this resource')
        parser.add_argument('decimal_val', type=float, help='Rate to charge for this resource')
        args = parser.parse_args()

        UID = args['uid']
        sensor_name = args['sensor_name']
        val = args['decimal_val']

        u = User.get(id=UID)
        if(u is None):
            return "User with this ID does not exist\n"

        s = Sensor.get(name=sensor_name)
        if(s is None):
            s = Sensor(name=sensor_name)

        v = Value(sensor=s, user=u, time=datetime.datetime.now())

        return jsonify(sensor_name=sensor_name,
                       value_Added = v.to_dict())
    except:
        return "404 Error"


if __name__ == '__main__':
    app.wsgi_app = orm.db_session(app.wsgi_app)
    app.run(debug=True)

