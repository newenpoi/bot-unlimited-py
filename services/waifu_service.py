from datetime import datetime
from dataclasses import dataclass
from typing import Union
from models.base import Database

@dataclass
class Waifu:
    id: int
    name: str
    gender: str
    origin: str
    price: int
    date_added: datetime
    url: str
    source: str

def add_user_waifu(identifier: int, server: int, waifu: int):
    '''Ajoute cette waifu à l'utilisateur sur ce serveur.'''
    with Database() as db:
        return db.execute(f'insert into users_waifus (waifu_id, user_id_unique, user_id_server) values ({waifu}, {identifier}, {server})')

def find_waifu(identifier: int, server: int, waifu: int):
    '''Récupère la dernière waifu de l'utilisateur sur ce serveur.'''
    with Database() as db:
        return db.find_one(f'select waifus.name, waifus.url, acquired from users_waifus inner join waifus on waifus.id = users_waifus.waifu_id where user_id_unique = {identifier} and user_id_server = {server} and waifu_id = {waifu}')