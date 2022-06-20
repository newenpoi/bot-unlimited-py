import nextcord
import config.settings as settings
import os

from nextcord.ext.commands import Bot
from os import environ
from dotenv import load_dotenv
from models import db
from services import element_service

# import platform, asyncio
# if platform.system() == 'Windows': asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
token = environ["TOKEN"]
if not token: exit("Aucun token n'est spécifié dans votre environnement.")

# Initialisation de l'ORM avec les coordonnées spécifiées...
db.bind(**settings.db_params)
db.generate_mapping(create_tables = True)

# Initialisation des tables.
element_service.init()

intents = nextcord.Intents().default(); intents.members = True
client = Bot(intents = intents)
client.remove_command('help')

# Loads each commands and events as extensions.
for folder, subfolders, files in os.walk('cogs'):
    for file in files:
        # Désolé pour cette syntaxe qui charge les extensions des dossiers commands et events !
        if file.endswith('py'): client.load_extension(f'{folder}.{file[:-3]}'.replace(os.sep, '.'))

client.run(token)