from datetime import datetime
from typing import List
from pony.orm import *
from models import Interaction, User_Interaction

@db_session
def init() -> None:
    '''Initialise les données de la table Interaction.'''
    
    if (len(select(e for e in Interaction)) == 0):
        Interaction(name = "Roue")
        Interaction(name = "Soulever")
        Interaction(name = "Penis")

@db_session
def find_all() -> List[Interaction]:
    '''Returns all interactions.'''
    return select(e for e in Interaction)
    
@db_session
def add_interaction(name: str) -> None:
    # Registers a new record.
    Interaction(name = name)

@db_session
def delete_interaction_where_timestamp_exceed(timespan: int):
    delete (i for i in User_Interaction if ((datetime.now - i.timestamp) > timespan))