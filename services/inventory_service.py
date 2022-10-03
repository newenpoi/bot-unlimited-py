from datetime import datetime
from time import strftime

from typing import List
from models.base import Database

def add_user_item(user: int, server: int, item: int, quantity: int = 1, stackable: int | None = None):
    with Database() as db:
        return db.execute(f'insert into inventories (user_id_unique, user_id_server, item_id, stackable, quantity) values ({user}, {server}, {item}, {stackable}, {quantity}) on duplicate key update quantity = quantity + {quantity}')