from pony.orm import *
from .base import db

class Element(db.Entity):
    id_unique = PrimaryKey(int, size = 64)
    name = Required(str, max_len = 32)
    users = Set("User")