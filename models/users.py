from pony.orm import *
from .base import db

from datetime import datetime

class User(db.Entity):
    id_unique = PrimaryKey(int, size = 64)
    id_server = Required(int, size = 64)
    name = Required(str, max_len = 32)
    gold = Required(int)
    tick = Required(datetime, sql_default = 'CURRENT_TIMESTAMP')
    element = Required("Element")