import re
from typing import List
from models.base import Database

def bind_server(server: int, channel: int):
    with Database() as db:
        db.execute(f'insert into bindings (id_server, id_channel) values ({server}, {channel}) on duplicate key update id_channel = {channel}')

def find_bound_channel(server: int):
    with Database() as db:
        return db.find_one(f'select id_channel as channel from bindings where id_server = {server}')