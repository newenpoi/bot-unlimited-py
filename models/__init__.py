from .base import Database

from .language import Language
from .element import Element
from .scoreboard import Scoreboard
from .user import User
from .interaction import Interaction
from .binding import Binding
from .role import Role

from .waifu import Waifu
from .user_waifu import User_Waifu
from .user_pull import User_Pull

from .category import Category
from .rarity import Rarity
from .item import Item

from .inventory import Inventory

def setup():
    with Database() as db:
        
        # Ajout des langages principaux de l'application (la création de cette table doit être exécutée en premier).
        db.execute(Language.model)
        if not db.count('languages') or db.count('languages') != len(Language.data): [db.execute(e) for e in Language.data]
        
        db.execute(Element.model)
        if not db.count('elements') or db.count('elements') != len(Element.data): [db.execute(e) for e in Element.data]

        db.execute(Scoreboard.model)
        db.execute(User.model)
        
        # Could be a @ManyToMany relationship in the future.
        db.execute(Interaction.model)
        
        db.execute(Binding.model)
        db.execute(Role.model)

        # @ManyToMany relationships.
        db.execute(Waifu.model)
        db.execute(User_Pull.model)
        db.execute(User_Waifu.model)
        if not db.count('waifus') or db.count('waifus') != len(Waifu.data): [db.execute(e) for e in Waifu.data]

        # Ajout de la structure et des données de catégories.
        db.execute(Category.model)
        if not db.count('categories') or db.count('categories') != len(Category.data): [db.execute(e) for e in Category.data]

        # Ajout de la structure et des données de raretés.
        db.execute(Rarity.model)
        if not db.count('rarities') or db.count('rarities') != len(Rarity.data): [db.execute(e) for e in Rarity.data]

        # Ajout de la structure et des données des objets.
        db.execute(Item.model)
        if not db.count('items') or db.count('items') != len(Item.data): [db.execute(e) for e in Item.data]

        db.execute(Inventory.model)
