from datetime import datetime
from time import strftime

from typing import List
from models.base import Database

def delete_heuristic_interaction(interaction: str, timespan: int):
    with Database() as db:
        return db.execute(f'delete from interactions where interactions.name = "{interaction}" and (timestampdiff(second, timestamp, now()) >= {timespan})')

def find_user_interaction_count(user: int, server: int, interaction: str) -> int:
    '''Renvoie le nombre d'interactions spécifique d'un utilisateur.'''
    with Database() as db:
        structure = db.find_one(f'select count(*) as n from interactions where user_id_unique = {user} and user_id_server = {server} and name = "{interaction}"')
        return structure.n

def find_interaction_count(server: int, interaction: str) -> int:
    '''Renvoie le nombre d'interactions spécifique du serveur.'''
    with Database() as db:
        structure = db.find_one(f'select count(*) as n from interactions where user_id_server = {server} and name = "{interaction}"')
        return structure.n

def add_interaction(user: int, server: int, interaction: str):
    with Database() as db:
        return db.execute(f'insert into interactions (name, user_id_unique, user_id_server) values ("{interaction}", {user}, {server})')

def find_interaction_timestamp(user: int, server: int, interaction: str):
    with Database() as db:
        return db.find_one(f'select timestamp from interactions where user_id_unique = {user} and user_id_server = {server} and name = "{interaction}"')