from datetime import datetime
from time import strftime

from typing import List, TypeVar
from models.base import Database

from dataclasses import dataclass

@dataclass
class Category:
    id: int
    name: str

@dataclass
class Rarity:
    id: int
    translation_id: int

@dataclass
class Item:
    id: int
    name: str
    description: str
    value: int
    category: Category
    rarity: Rarity

ItemType = TypeVar('ItemType', bound = Item)

def find_item_by_category_and_random():
    with Database() as db:
        item = db.find_one('select categories.name as category, rarities.id as rarity_id, rarities.translation_id as rarity, items.id, items.name, description, value from items inner join categories on categories.id = category_id inner join rarities on rarities.id = rarity_id order by rand() limit 1')
        
        # Category.
        category = Category(id = 1, name = item.category)

        # Rarity.
        rarity = Rarity(id = item.rarity_id, translation_id = item.rarity)

        # Convert any type to the correct object using interface modularity.
        response = Item(id = item.id, name = item.name, description = item.description, value = item.value, category = category, rarity = rarity)
        
        # The response is a item object.
        return response
