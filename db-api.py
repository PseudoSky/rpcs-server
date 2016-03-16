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


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):    
    try:
        return jsonify({'first': User[user_id].first,
                'last' : User[user_id].last,
                'phone': User[user_id].phone,
                'address': User[user_id].address})
    except:
        return "404 Error"

#fix DIS
@app.route('/api/user/', methods=['POST'])
def make_user():
    new_id = db.insert("User", first="aditya", last="bist", phone="12213123123", address="23sdfs", classType="User", 
        returning='id')
    return jsonify({'new_id' : new_id})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.wsgi_app = orm.db_session(app.wsgi_app)
    app.run(debug=True)

