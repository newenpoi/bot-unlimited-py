import asyncio
import nextcord

from nextcord import Client
from nextcord.ext.commands import Cog
from pony.orm import *

from utils.activity import ActivityType
from services import user_service

class Ready(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    async def syncs(self, timer):
        while True:
            # Syncs the members of every guilds with the database.
            for guild in self.client.guilds:
                
                # Gets the amount of members synced in the database in this server.
                rows = user_service.find_all_users_ids_from_guild(guild.id)
                syncs = 0
                
                # Makes the comparison with the members (also includes bots) present in the guild.
                if len(rows) < (guild.member_count):
                    # Syncs every member of the server that is not synchronized yet.
                    for member in guild.members:
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
    
    @Cog.listener()
    async def on_ready(self):

        # Shows a classical console alert for loggin in.
        print(f'\n{self.client.user} connecté avec succès.')

        # Logs how many guilds we are connected to.
        print(f'{len(self.client.guilds)} Guilde(s).')

        # Setting the bot's activity (status).
        await self.client.change_presence(status = nextcord.Status.online, activity = nextcord.Activity(name = "les échos des âmes.", type = ActivityType.listening))

        # Periodically syncs new users of guilds into database if there is.
        await asyncio.create_task(self.syncs(60))

def setup(bot: Client) -> None:
    bot.add_cog(Ready(bot))