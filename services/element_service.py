from datetime import datetime
from typing import List
from pony.orm import *
from models import Element

@db_session
def init() -> None:
    '''Initialise les données de la table Elements.'''
    
    if (len(select(e for e in Element)) == 0):
        Element(name = "Haine")
        Element(name = "Pêché")
        Element(name = "Consolation")
        Element(name = "Clémence")
        Element(name = "Supplice")
        Element(name = "Vertu")


@db_session
def find_all() -> List[Element]:
    '''Renvoie tous les éléments'''
    return select(e for e in Element)
    
@db_session
def add_element(name: str) -> None:
    # Makes the check if this element already exists (constraint violation).
    if (Element.exists(name = name)): print("Cet élément existe déjà (contrainte délenchée)."); return

    # Registers a new record.
    Element(name = name)
