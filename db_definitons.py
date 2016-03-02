from datetime import datetime
from decimal import Decimal
from pony.orm import *
​
db = Database("sqlite", "database.sqlite", create_db=True)
​
class Sensor(db.Entity):
    name = PrimaryKey(str)
    values = Set("Value")
​
​
class Value(db.Entity):
    sensor = Required(Sensor)
    user = Required("User")
    time = Required(datetime)
    value = Optional(Decimal)
    PrimaryKey(sensor, user, time)
​
​
class User(db.Entity):
    id = PrimaryKey(int)
    first = Required(str)
    last = Required(str)
    phone = Optional(str)
    address = Optional(LongStr)
    values = Set(Value)
    users_from = Set("UserUser", reverse="user_from")
    users_to = Set("UserUser", reverse="user_to")
​
​
class Patient(db.User):
    pass
​
​
class CareGiver(db.User):
    pass
​
​
class Medicine(db.Sensor):
    pass
​
​
class UserUser(db.Entity):
    active = Required(bool)
    created_on = Required(datetime)
    user_from = Required(User, reverse="users_from")
    user_to = Required(User, reverse="users_to")
​
​
class Doctor(db.User):
    pass
​
​
class DoctorPatient(db.UserUser):
    pass
​
​
class CarePatient(db.UserUser):
    pass
​
​
class Sleep(db.Sensor):
    pass
​
​
class Step(db.Sensor):
    pass
​
​
class HeartRate(db.Sensor):
    pass
​
​
class Location(db.Sensor):
    pass
​
​
class Activity(db.Sensor):
    pass
​
​
class Weight(db.Sensor):
    pass
​
​
class Question(db.Sensor):
    form = Required("Form")
​
​
class Form(db.Entity):
    id = PrimaryKey(int, auto=True)
    questions = Set(Question)
​
​
sql_debug(True)
db.generate_mapping(create_tables=True)