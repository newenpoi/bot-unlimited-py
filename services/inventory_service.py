from typing import Union
from models.base import Database

def add_inventory_item(user: int, server: int, item: int, quantity: int = 1, stackable: Union[int, None] = None):
    '''Ajoute un objet à l'inventaire de l'utilisateur.'''
    with Database() as db:
        return db.execute(f'insert into inventories (user_id_unique, user_id_server, item_id, stackable, quantity) values ({user}, {server}, {item}, {stackable}, {quantity}) on duplicate key update quantity = quantity + {quantity}')

def remove_inventory_item(user: int, server: int, item: int, quantity: int = 1):
    '''Retire un objet de l'inventaire de l'utilisateur.'''
    with Database() as db:
        # Updates item if stackable and high than one.
        items = db.execute(f'select quantity from inventories where user_id_unique = {user} and user_id_server = {server} and item_id = {item}')
        
        if items is not None and items.quantity > 1: return db.execute(f'update inventories where user_id_unique = {user} and user_id_server = {server}')
        
        return db.execute(f'delete from inventories where user_id_unique = {user} and user_id_server = {server}')
        