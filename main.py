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

class CustomClient():
    def __init__(self, intents):
        self.client = Bot(intents = intents)
        self.client.remove_command('help')
        
        load_dotenv()
        self.token = environ["TOKEN"]
        if not self.token: exit("Aucun token n'est spécifié dans votre environnement.")

        self.init_services()
        self.load_extensions()
        self.client.run(self.token)

    def init_services(self):
        element_service.init()
        interaction_service.init()
        
    def load_extensions(self):
        for f in [f'cogs.events.{f[:-3]}' for f in os.listdir((Path(__file__).parent / "cogs/events")) if f.endswith('py')]: self.client.load_extension(f)
        for f in [f'cogs.commands.{f[:-3]}' for f in os.listdir((Path(__file__).parent / "cogs/commands")) if f.endswith('py')]: self.client.load_extension(f)
        
if __name__ == '__main__':
    intents = nextcord.Intents().default(); intents.members = True; intents.message_content = True
    client = CustomClient(intents)