from models.base import Database

def add_entry(identifier: int, server: int, score: int):
    '''Ajoute une nouvelle entrée dans la table quiz.'''
    with Database() as db:
        return db.execute(f'insert into quiz (user_id_unique, user_id_server, score, timing) values ({identifier}, {server}, {score}, 0)')

def find_score(server: int):
    '''Récupère le total des scores du quiz sur ce serveur.'''
    with Database() as db:
        result = db.find_all(f'select user_id_unique, sum(score) as score from quiz where user_id_server = {server} group by user_id_unique')
        return result

def cleanup_score(server: int):
    '''Nettoie le score du quiz.'''
    with Database() as db:
        return db.execute(f'delete from quiz where user_id_server = {server}')