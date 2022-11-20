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

@dataclass
class Pull:
    id: int
    user_id_unique: int
    user_id_server: int
    waifu: Waifu
    created: datetime

def add_user_pull(identifier: int, server: int):
    '''Ajoute une pioche de waifu à cet utilisateur sur ce serveur.'''
    with Database() as db:
        return db.execute(f'insert into users_pulls (user_id_unique, user_id_server, waifu_id) values ({identifier}, {server}, FLOOR(1 + RAND() * (select count(*) from waifus)))')

def find_pull(identifier: int, server: int) -> Union[Pull, None]:
    '''Récupère la waifu piochée.'''
    with Database() as db:
        pull = db.find_one(f'select waifus.name, waifus.gender, waifus.origin, waifus.price, waifus.url, waifus.source, users_pulls.waifu_id, users_pulls.created from users_pulls inner join waifus on waifus.id = users_pulls.waifu_id where user_id_unique = {identifier} and user_id_server = {server} order by users_pulls.id desc limit 1')

        if not pull: return None
        
        waifu = Waifu(id = pull.waifu_id, name = pull.name, gender = pull.gender, origin = pull.origin, price = pull.price, url = pull.url, source = pull.source)
        return Pull(waifu = waifu, created = pull.created)