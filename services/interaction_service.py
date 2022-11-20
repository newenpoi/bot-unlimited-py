from datetime import datetime
from time import strftime

from typing import List, TypeVar
from models.base import Database

from dataclasses import dataclass

@dataclass
class Interaction:
    id: int
    name: str
    timestamp: datetime

# InteractionType = TypeVar('InteractionType', bound = Interaction)

def delete_heuristic_interaction(interaction: str, timespan: int):
    with Database() as db:
        return db.execute(f'delete from interactions where interactions.name = "{interaction}" and (timestampdiff(second, timestamp, now()) >= {timespan})')

def find_user_interaction_count(user: int, server: int, interaction: str) -> int:
    '''Renvoie le nombre d'interactions de l'utilisateur pour ce module (interaction).'''
    with Database() as db:
        structure = db.find_one(f'select count(*) as n from interactions where user_id_unique = {user} and user_id_server = {server} and name = "{interaction}"')
        return structure.n

def find_interaction_timestamp(user: int, server: int, interaction: str):
    '''Renvoie la date à laquelle a eu lieu la dernière interaction de ce module.'''
    with Database() as db:
        interaction = db.find_one(f'select id, name, timestamp from interactions where user_id_unique = {user} and user_id_server = {server} and name = "{interaction}"')
        if not interaction: return None
        
        return Interaction(id = interaction.id, name = interaction.name, timestamp = interaction.timestamp)

def find_interaction_count(server: int, interaction: str) -> int:
    '''Renvoie le nombre d'interactions spécifique du serveur.'''
    with Database() as db:
        structure = db.find_one(f'select count(*) as n from interactions where user_id_server = {server} and name = "{interaction}"')
        return structure.n

def add_interaction(user: int, server: int, interaction: str):
    '''Ajoute une interaction à cet utilisateur sur ce serveur.'''
    with Database() as db:
        return db.execute(f'insert into interactions (name, user_id_unique, user_id_server) values ("{interaction}", {user}, {server})')