from .base import db
from .users import User
from .elements import Element

import config.settings as settings

# Initialisation de l'ORM avec les coordonnées spécifiées...
def setup():
    db.bind(**settings.db_params)
    db.generate_mapping(create_tables = True)