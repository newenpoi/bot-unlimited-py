from typing import List
from models.base import Database

def add_role(server: int, channel: int, message: int, role: int, emoji: str):
    with Database() as db:
        # TODO : Faille sécurité avec l'emoji ?
        return db.execute(f'insert into roles (id_server, id_channel, id_message, id_role, emoji) values ({server}, {channel}, {message}, {role}, "{emoji}")')

def find_role(server: int, channel: int, message: int, emoji: str):
    '''Renvoie l'emoji qui correspond à un message de gestion des rôles sur un canal et serveur donné.'''
    with Database() as db:
        # TODO : Faille sécurité avec l'emoji ?
        return db.find_one(f'select id_role, emoji from roles where id_server = {server} and id_channel = {channel} and id_message= {message} and emoji = "{emoji}"')

def find_role_globally(server: int, channel: int, role: int):
    '''Renvoie le rôle géré globallement par le serveur si ce dernier existe.'''
    with Database() as db:
        return db.find_one(f'select id_role from roles where id_server = {server} and id_channel = {channel} and id_role = {role}')

def delete_role(role: int):
    '''Supprime le rôle via son identifiant.'''
    with Database() as db:
        return db.execute(f'delete from roles where id_role = {role}')