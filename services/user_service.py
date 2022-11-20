import re
from typing import List
from models.base import Database

def add_user(identifier: int, server: int, nickname: str):
    with Database() as db:
        return db.execute(f'insert into users (id_unique, id_server, nickname) values ({identifier}, {server}, "{re.escape(nickname)}")')

def find_all_user_id_having_server(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique from users where id_server = {server}')

def find_users_having_birthday(server: int) -> list:
    with Database() as db:
        return db.find_all(f'select id_unique as id, date_birth as date, show_date_birth as display from users where id_server = {server} and month(date_birth) = month(now()) and day(date_birth) = day(now())')

def find_user(identifier: int, server: int):
    '''Récupère les données de l'utilisateur sur le serveur.'''
    with Database() as db:
        return db.find_one(f'select id_unique, id_server, nickname, gold, tick, element, health from users where id_unique = {identifier} and id_server = {server}')

def find_health(identifier: int, server: int) -> int:
    '''Renvoie les points de vie de cet utilisateur sur ce serveur.'''
    with Database() as db:
        structure = db.find_one(f'select health from users where id_unique = {identifier} and id_server = {server}')
        return structure.health

def find_birthday(identifier: int) -> str:
    '''Renvoie l'anniversaire du membre.'''
    with Database() as db:
        structure = db.find_one(f'select date_birth as date from users where id_unique = {identifier}')
        return structure.date

def find_gold(identifier: int, server: int) -> int:
    '''Récupère les crédits de l'utilisateur.'''
    with Database() as db:
        structure = db.find_one(f'select gold from users where id_unique = {identifier} and id_server = {server}')
        return structure.gold

def edit_health(identifier: int, server: int, health: int):
    '''Modifie les points de vie de cet utilisateur sur le serveur.'''
    with Database() as db:
        return db.execute(f'update users set health = health + {health} where id_unique = {identifier} and id_server = {server}')

def edit_birthday(identifier: int, server: int, date: str, show: bool):
    '''Modifie la date d'anniversaire du membre du serveur.'''
    with Database() as db:
        return db.execute(f'update users set date_birth = str_to_date("{date}", "%d/%m/%Y"), show_date_birth = {show} where id_unique = {identifier} and id_server = {server}')

def edit_gold(identifier: int, server: int, gold: int):
    '''Modifie la somme d'argent de cet utilisateur sur ce serveur.'''
    with Database() as db:
        return db.execute(f'update users set gold = gold + {gold} where id_unique = {identifier} and id_server = {server}')

def remove_user(identifier: int, server: int):
    '''Supprime l'utilisateur de la base de données.'''
    with Database() as db:
        return db.execute(f'delete from users where id_unique = {identifier} and id_server = {server}')
