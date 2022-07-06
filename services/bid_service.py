import random
from typing import List
from models.base import Database

def rotate(server: int):
    with Database() as db:
        return db.execute(f'insert into bids (id_server, waifu_id) values ({server}, floor(1 + rand() * (select count(*) from waifus)))')

def find_today_bid(server: int):
    with Database() as db:
        return db.find_one(f'select waifus.name, waifus.price, waifus.source, date_last_bid from bids inner join waifus on waifus.id = bids.waifu_id where id_server = {server} order by bids.id desc limit 1')