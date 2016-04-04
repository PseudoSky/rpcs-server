#!flask/bin/python
from flask import Flask, jsonify,request
from db_definitions import *
import flask.ext.restful as rest
from pony import orm

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

#retrieve a user
@app.route('/api/user', methods=['GET'])
def get_users(user_id):    
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
    # print(str(request.form))
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

if __name__ == '__main__':
    app.wsgi_app = orm.db_session(app.wsgi_app)
    app.run(host='128.2.20.131', port=5000, debug=True)

