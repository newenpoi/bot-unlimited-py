from .base import Database

from .element import Element
from .scoreboard import Scoreboard
from .user import User
from .interaction import Interaction
from .binding import Binding
from .role import Role

from .waifu import Waifu
from .user_waifu import User_Waifu
from .user_pull import User_Pull

def setup():
    with Database() as db:
        
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

        
