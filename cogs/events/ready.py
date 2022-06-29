import asyncio
import nextcord
from datetime import datetime

from nextcord import Client
from nextcord.ext.commands import Cog
from pony.orm import *

from utils import helper
from utils.activity import ActivityType
from services import user_service, interaction_service, scoreboard_service

class Ready(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    async def syncs(self, timer):
        while True:
            # Syncs the members of every guilds with the database.
            for guild in self.client.guilds:
                
                # Gets the amount of members synced in the database in this server.
                rows = user_service.find_all_user_id_having_server(guild.id)
                syncs = 0
                
                # Makes the comparison with the members (also includes bots) present in the guild.
                if len(rows) < (guild.member_count):
                    # Syncs every member of the server that is not synchronized yet.
                    for member in guild.members:
                        # TODO : Sync user display name.
                        # If this guild member id is not present in rows.
                        if member.id not in rows:
                            # Adds a new record for this user.
                            print(f'Synchronisation du membre : {member.id} avec pour pseudo {member.display_name}...')
                            user_service.add_user(member.id, member.guild.id, member.display_name)
                            syncs = syncs + 1

                # Shows the number of synced users.
                if syncs: print(f'Synchronisation de {syncs} utilisateurs pour la guilde {guild.name}.')
            
            # Sleeps for a determined amount of time.
            await asyncio.sleep(timer)
    
    async def clean(self, timer):
        while True:
            interactions = {'soulever': 3000, 'roue': 43200, 'epenis': 86400}

            for interaction, timespan in interactions.items():
                # Removes the interactions from database that exceeded a certain timespan.
                interaction_service.delete_heuristic_interaction(interaction, timespan)

            # Wipes the scoreboard every 24 hours.
            if (helper.temporal(datetime.now())[:-3] == '18:00'):
                # Gets the winner of every server.
                scores = scoreboard_service.find_top_scores()
                
                # Clears the scoreboard of every server.
                scoreboard_service.truncate_scoreboard()

                # Show the winner of every server.
                for score in scores: print(score.unit)
            
            await asyncio.sleep(timer)
    
    @Cog.listener()
    async def on_ready(self):

        # Shows a classical console alert for loggin in.
        print(f'\n{self.client.user} connecté avec succès.')

        # Logs how many guilds we are connected to.
        print(f'{len(self.client.guilds)} Guilde(s).')

        # Setting the bot's activity (status).
        await self.client.change_presence(status = nextcord.Status.online, activity = nextcord.Activity(name = "les échos des âmes.", type = ActivityType.listening))

        # Periodically syncs new users of guilds into database if there is.
        await asyncio.gather(self.syncs(60), self.clean(60))

def setup(bot: Client) -> None:
    bot.add_cog(Ready(bot))