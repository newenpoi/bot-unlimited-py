from datetime import datetime
from typing import List
from pony.orm import *
from models import User

@db_session
def find_all() -> List[User]:
    '''Renvoie tous les utilisateurs'''
    return select(u for u in User)

@db_session
def find_all_users_ids_from_guild(guild_id: int) -> List[int]:
    # return User.select_by_sql(f'select id_unique from user where id_server = ${guild_id}')
    users = select (u.id_unique for u in User if u.id_server == guild_id)[:]
    return users
    
@db_session
def add_user(id_unique: int, id_server: int, name: str) -> None:
    # Makes the check if this user already exists (constraint violation).
    if (User.exists(id_unique = id_unique)): print("Cet utilisateur existe déjà (contrainte délenchée)."); return

    # Registers a new record.
    User(id_unique = id_unique, id_server = id_server, name = name, gold = 500, tick = datetime.now())

