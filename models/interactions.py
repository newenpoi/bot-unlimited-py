from datetime import datetime
from pony.orm import *
from .base import db
from .users import User

class Interaction(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str, 32, unique = True)
    users = Set('User_Interaction')

class User_Interaction(db.Entity):
    id = PrimaryKey(int, auto = True)
    user = Required(User)
    interaction = Required(Interaction)
    timestamp = Required(datetime, default = datetime.now)