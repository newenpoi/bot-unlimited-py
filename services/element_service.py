from datetime import datetime
from typing import List
from pony.orm import *
from models import Element

@db_session
def init() -> None:
    '''Initialise les données de la table Elements.'''
    Element(name = "Wrath")
    Element(name = "Sin")

@db_session
def find_all() -> List[Element]:
    '''Renvoie tous les éléments'''
    return select(e for e in Element)
    
@db_session
def add_element(id_unique: int, name: str) -> None:
    # Makes the check if this element already exists (constraint violation).
    if (Element.exists(id_unique = id_unique)): print("Cet élément existe déjà (contrainte délenchée)."); return

    # Registers a new record.
    Element(id_unique = id_unique, name = name)
