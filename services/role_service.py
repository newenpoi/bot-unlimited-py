from typing import List
from models.base import Database

def add_role(server: int, channel: int, message: int, role: int, emoji: str):
    with Database() as db:
        # Code.
        return None