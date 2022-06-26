from .base import db
from .users import User
from .elements import Element
from .interactions import Interaction
from .scoreboard import Scoreboard

import config.settings as settings

def setup():
    db.bind(**settings.db_params)
    db.generate_mapping(create_tables = True)