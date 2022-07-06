import re
from typing import List
from models.base import Database

# TODO : Déclarer une Interface

def find_all_user_id_having_server(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique from users where id_server = {server}')

def find_users_having_birthday(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique as id, date_birth as date, show_date_birth as show from users where id_server = {server} and month(date_birth) = month(now()) and day(date_birth) = day(now())')

def add_user(identifier: int, server: int, nickname: str):
    with Database() as db:
        return db.execute(f'insert into users (id_unique, id_server, nickname) values ({identifier}, {server}, "{re.escape(nickname)}")')

def find_health(identifier: int, server: int) -> int:
    with Database() as db:
        structure = db.find_one(f'select health from users where id_unique = {identifier} and id_server = {server}')
        return structure.health

def find_birthday(identifier: int) -> str:
    with Database() as db:
        structure = db.find_one(f'select date_birth as date from users where id_unique = {identifier}')
        print(structure)
        return structure.date

def find_gold(identifier: int, server: int) -> int:
    with Database() as db:
        structure = db.find_one(f'select gold from users where id_unique = {identifier} and id_server = {server}')
        print(structure)
        return structure.gold

def edit_health(identifier: int, server: int, health: int):
    with Database() as db:
        return db.execute(f'update users set health = health + {health} where id_unique = {identifier} and id_server = {server}')

def edit_birthday(identifier: int, server: int, date: str, show: bool):
    with Database() as db:
        return db.execute(f'update users set date_birth = str_to_date("{date}", "%d/%m/%Y"), show_date_birth = {show} where id_unique = {identifier} and id_server = {server}')

def edit_gold(identifier: int, server: int, gold: int):
    with Database() as db:
        return db.execute(f'update users set gold = gold + {gold} where id_unique = {identifier} and id_server = {server}')
