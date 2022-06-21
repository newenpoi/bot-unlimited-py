from pony.orm import *
from .base import db
from .users import User

class Element(db.Entity):
    id_unique = PrimaryKey(int, size = 64, auto = True)
    name = Required(str, 32, unique = True)
    users = Set(User)