from datetime import datetime
from typing import List
from pony.orm import *
from models import User, Element, Interaction, User_Interaction

@db_session
def find_all() -> List[User]:
    '''Renvoie tous les utilisateurs'''
    return select(u for u in User)

@db_session
def find_all_users_ids_from_guild(guild_id: int) -> List[int]:
    return select (u.id_unique for u in User if u.id_server == guild_id)[:]
    
@db_session
def add_user(id_unique: int, id_server: int, nickname: str) -> None:
    # Registers a new record.
    User(id_unique = id_unique, id_server = id_server, nickname = nickname, element = Element.get(id_unique = 1))

@db_session
def find_user_interactions_having(user_id: int, name: str) -> int:
    '''Renvoie les userinteractions spécifiés par le nom de l'interaction pour cet utilisateur.'''
    return select (userinteraction for userinteraction in User[user_id].interactions if userinteraction.interaction.name == name)[:]

@db_session
def find_user_health(user_id: int) -> int:
    '''Renvoie le nombre de points de vie de cet utilisateur.'''
    return User[user_id].health

@db_session
def update_health(user_id: int, health: int) -> None:
    '''Modifie les points de vie de l'utilisateur.'''
    User[user_id].health += health

@db_session
def add_interaction(identifier: int, name: str) -> None:
    User[identifier].interactions.add(User_Interaction(user = identifier, interaction = Interaction.get(name = name)))