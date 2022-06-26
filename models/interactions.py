from datetime import datetime
from pony.orm import *
from .base import db
from .users import User

class Interaction(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str, 32)
    timestamp = Required(datetime, default = lambda: datetime.now())
    user = Required('User')
    