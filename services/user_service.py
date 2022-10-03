import re
from typing import List
from models.base import Database

# TODO : Déclarer une Interface

def find_all_user_id_having_server(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique from users where id_server = {server}')

def find_users_having_birthday(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique as id, date_birth as date, show_date_birth as display from users where id_server = {server} and month(date_birth) = month(now()) and day(date_birth) = day(now())')

def find_user(identifier: int, server: int):
    with Database() as db:
        return db.find_one(f'select gold, tick, element, health from users where id_unique = {identifier} and id_server = {server}')

def add_user(identifier: int, server: int, nickname: str):
    with Database() as db:
        return db.execute(f'insert into users (id_unique, id_server, nickname) values ({identifier}, {server}, "{re.escape(nickname)}")')

def add_user_pull(identifier: int, server: int):
    with Database() as db:
        return db.execute(f'insert into users_pulls (user_id_unique, user_id_server, waifu_id) values ({identifier}, {server}, FLOOR(1 + RAND() * (select count(*) from waifus)))')

def add_user_waifu(identifier: int, server: int, waifu: int):
    with Database() as db:
        return db.execute(f'insert into users_waifus (waifu_id, user_id_unique, user_id_server) values ({waifu}, {identifier}, {server})')

def find_health(identifier: int, server: int) -> int:
    with Database() as db:
        structure = db.find_one(f'select health from users where id_unique = {identifier} and id_server = {server}')
        return structure.health

def find_birthday(identifier: int) -> str:
    with Database() as db:
        structure = db.find_one(f'select date_birth as date from users where id_unique = {identifier}')
        return structure.date

def find_gold(identifier: int, server: int) -> int:
    with Database() as db:
        structure = db.find_one(f'select gold from users where id_unique = {identifier} and id_server = {server}')
        return structure.gold

def find_waifu(identifier: int, server: int, waifu: int):
    with Database() as db:
        return db.find_one(f'select waifus.name, waifus.url, acquired from users_waifus inner join waifus on waifus.id = users_waifus.waifu_id where user_id_unique = {identifier} and user_id_server = {server} and waifu_id = {waifu}')

def find_user_pull(identifier: int, server: int):
    with Database() as db:
        return db.find_one(f'select waifus.name, waifus.gender, waifus.origin, waifus.price, waifus.url, waifus.source, users_pulls.waifu_id from users_pulls inner join waifus on waifus.id = users_pulls.waifu_id where user_id_unique = {identifier} and user_id_server = {server} order by users_pulls.id desc limit 1')

def edit_health(identifier: int, server: int, health: int):
    with Database() as db:
        return db.execute(f'update users set health = health + {health} where id_unique = {identifier} and id_server = {server}')

def edit_birthday(identifier: int, server: int, date: str, show: bool):
    with Database() as db:
        return db.execute(f'update users set date_birth = str_to_date("{date}", "%d/%m/%Y"), show_date_birth = {show} where id_unique = {identifier} and id_server = {server}')

def edit_gold(identifier: int, server: int, gold: int):
    with Database() as db:
        return db.execute(f'update users set gold = gold + {gold} where id_unique = {identifier} and id_server = {server}')
