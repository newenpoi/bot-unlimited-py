from typing import List, TypeVar
from models.base import Database

from dataclasses import dataclass

@dataclass
class Scoreboard:
    id_unique: int
    id_server: int
    value: int
    unit: str
    scale: int

ScoreboardType = TypeVar('ScoreboardType', bound = Scoreboard)

'''
def find_top_scores():
    with Database() as db:
        return db.find_all('select scoreboard.value, scoreboard.unit from scoreboard group by id_server order by scoreboard.value desc, scoreboard.scale desc')
'''

def find_top_score(server: int):
    with Database() as db:
        return db.find_one(f'select scoreboard.id_unique as user, scoreboard.value, scoreboard.unit from scoreboard where id_server = {server} order by scoreboard.value desc, scoreboard.scale desc')

def truncate_scoreboard():
    with Database() as db:
        return db.execute('truncate table scoreboard')

def find_score(identifier: int, server: int):
    '''Renvoie les données du score du membre du serveur.'''
    with Database() as db:
        scoreboard = db.find_one(f'select id_unique, id_server, value, unit, scale from scoreboard where id_unique = {identifier} and id_server = {server}')
        
        # Renvoie un objet Scoreboard si des données sont récupérées.
        if scoreboard: scoreboard = Scoreboard(id_unique = scoreboard.id_unique, id_server = scoreboard.id_server, value = scoreboard.value, unit = scoreboard.unit, scale = scoreboard.scale)
        
        return scoreboard

def add_score(identifier: int, server: int, value: int, unit: str, scale: int):
    '''Ajoute les données du score de l'utilisateur depuis le module scoreboard sur ce serveur.'''
    with Database() as db:
        return db.execute(f'insert into scoreboard (id_unique, id_server, value, unit, scale) values ({identifier}, {server}, {value}, "{unit}", {scale})')
