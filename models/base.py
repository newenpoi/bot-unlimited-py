import mysql.connector
import config.settings as settings
import utils.helper as helper

'''
    Author : newenpoi
    
    *Please do not break something while manipuling this class.
'''

class Database:
    '''Fourni un accès MySQL.'''
    def __init__(self):
        """Gestion i/o de la base de données."""
        try:
            self._conn = mysql.connector.connect(**settings.db_params)
            self._cursor = self._conn.cursor(dictionary = True, buffered = True)
        except:
            exit("Le projet Hatada a besoin d'une connexion à MySQL pour être opérationnel.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._conn: self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor
    
    def commit(self):
        self.connection.commit()

    def close(self, commit = True):
        if commit: self.commit()
        self.connection.close()

    def execute(self, sql, params = None):
        try: self.cursor.execute(sql, params or ())
        except mysql.connector.errors.IntegrityError: pass

    def fetchone(self, list = False):
        return self.cursor.fetchone() if list else helper.nest(self.cursor.fetchone())

    def fetchall(self, list = False):
        return self.cursor.fetchall() if list else helper.nest(self.cursor.fetchall())

    def callproc(self, sql, params = []):
        return self.cursor.callproc(sql, params)

    def count(self, table: str):
        self.execute(f'select count(*) as n from `{table}`')
        return self.fetchone(list = True)['n']

    def find_one(self, sql: str):
        self.execute(sql)
        return self.fetchone()

    def find_all(self, sql: str):
        self.execute(sql)
        return self.fetchall()
