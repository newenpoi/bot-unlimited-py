from datetime import datetime
from time import strftime
from typing import List
from pony.orm import *
from models import Interaction, User
from utils import helper

@db_session
def find_all() -> List[Interaction]:
    '''Returns all interactions.'''
    return select (e for e in Interaction)

@db_session
def find_interaction_timestamp(identifier: int, server: int, name: str) -> datetime:
    '''
        Returns the timestamp from this interaction.
    '''
    return select (interaction.timestamp for interaction in Interaction if interaction.name == name and interaction.user == User[identifier, server]).first()
    
@db_session
def add_interaction(identifier: int, server: int, name: str) -> None:
    # Registers a new record.
    Interaction(name = name, user = User[identifier, server])

@db_session
def delete_interaction_where_timestamp_difference_exceed(interaction: str, timespan: int):
    Interaction.select(lambda i: i.name == interaction and i.timestamp >= raw_sql(f"datetime('now', '-{timespan} seconds', 'localtime')")).delete(bulk = True)