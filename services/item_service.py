from datetime import datetime
from time import strftime

from typing import List
from models.base import Database

def find_item_by_category_and_random():
    with Database() as db:
        return db.find_one('select categories.name as category, rarities.id as rarity_id, rarities.name as rarity, items.id, items.name, description, value from items inner join categories on categories.id = category_id inner join rarities on rarities.id = rarity_id order by rand() limit 1')