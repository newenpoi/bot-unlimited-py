from typing import List
from models.base import Database

def find_top_scores():
    with Database() as db:
        return db.find_all('select scoreboard.value, scoreboard.unit from scoreboard group by id_server order by scoreboard.value desc, scoreboard.scale desc')

def truncate_scoreboard():
    with Database() as db:
        return db.execute('truncate table scoreboard')

def find_score(identifier: int, server: int):
    with Database() as db:
        return db.find_one(f'select value, unit from scoreboard where id_unique = {identifier} and id_server = {server}')

def add_score(identifier: int, server: int, value: int, unit: str, scale: int):
    with Database() as db:
        return db.execute(f'insert into scoreboard (id_unique, id_server, value, unit, scale) values ({identifier}, {server}, {value}, "{unit}", {scale})')
