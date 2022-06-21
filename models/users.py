from pony.orm import *
from .base import db

from datetime import datetime

class User(db.Entity):
    id_unique = PrimaryKey(int, size = 64, auto = False)
    id_server = Required(int, size = 64)
    nickname = Required(str, 32)
    gold = Required(int, default = 500)
    tick = Required(datetime, default = lambda: datetime.now())
    element = Required('Element')