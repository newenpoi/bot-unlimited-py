from pathlib import Path
import nextcord
import os

import models
models.setup()

from nextcord.ext.commands import Bot
from os import environ
from dotenv import load_dotenv

from services import element_service
from services import interaction_service

# import platform, asyncio
# if platform.system() == 'Windows': asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

load_dotenv()
token = environ["TOKEN"]
if not token: exit("Aucun token n'est spécifié dans votre environnement.")

# Initialisation des données.
element_service.init()
interaction_service.init()

intents = nextcord.Intents().default(); intents.members = True; intents.message_content = True
client = Bot(intents = intents)
client.remove_command('help')

# Loads each commands and events as extensions (unix and windows path friendly).
for f in [f'cogs.events.{f[:-3]}' for f in os.listdir((Path(__file__).parent / "cogs/events")) if f.endswith('py')]: client.load_extension(f)
for f in [f'cogs.commands.{f[:-3]}' for f in os.listdir((Path(__file__).parent / "cogs/commands")) if f.endswith('py')]: client.load_extension(f)

client.run(token)