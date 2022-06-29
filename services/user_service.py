import re
from typing import List
from models.base import Database

def find_all_user_id_having_server(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique from users where id_server = {server}')

def add_user(identifier: int, server: int, nickname: str):
    with Database() as db:
        return db.execute(f'insert into users (id_unique, id_server, nickname) values ({identifier}, {server}, "{re.escape(nickname)}")')

def find_health(identifier: int, server: int):
    with Database() as db:
        structure = db.find_one(f'select health from users where id_unique = {identifier} and id_server = {server}')
        return structure.health

def edit_health(identifier: int, server: int, health: int):
    with Database() as db:
        return db.execute(f'update users set health = health + {health} where id_unique = {identifier} and id_server = {server}')
