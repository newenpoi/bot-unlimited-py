from .base import Database

from .element import Element
from .scoreboard import Scoreboard
from .interaction import Interaction
from .user import User

def setup():
    with Database() as db:
        
        db.execute(Element.model)
        if not db.count('elements') or db.count('elements') != len(Element.data): [db.execute(e) for e in Element.data]

        db.execute(Scoreboard.model)
        db.execute(User.model)
        db.execute(Interaction.model)
