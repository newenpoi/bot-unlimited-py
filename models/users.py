from pony.orm import *
from .base import db

from datetime import date, datetime

class User(db.Entity):
    id_unique = Required(int, size = 64, auto = False)
    id_server = Required(int, size = 64)
    nickname = Required(str, 32)
    gold = Required(int, default = 500)
    tick = Required(datetime, default = lambda: datetime.now())
    element = Required('Element')
    date_birth = Optional(date)
    health = Required(int, default = 100)
    interactions = Set('Interaction')
    PrimaryKey(id_unique, id_server)

    # Exemple de méthode personnalisée de l'entité User.
    def get_nickname_and_gold(self):
        return "%s (%s)" % (self.nickname, self.gold)