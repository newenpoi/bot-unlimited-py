import asyncio
import random
import nextcord
import requests

from datetime import datetime, timezone, timedelta
from bs4 import BeautifulSoup

from nextcord import Client, Embed
from nextcord.ext.commands import Cog

from utils import dateutils, reader, writer
from utils.activity import ActivityType
from services import user_service, interaction_service, scoreboard_service, binding_service

import config.settings as settings

class Ready(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    async def syncs(self, timer):
        '''Synchronizes users with the database.'''
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
        '''Periodically cleans interactions and scoreboard.'''
        while True:
            interactions = {'soulever': 3000, 'roue': 43200, 'epenis': 86400, 'waifu': 8400, 'mention': 21600, 'dig': 8400}

            for interaction, timespan in interactions.items():
                # Removes the interactions from database that exceeded a certain timespan.
                interaction_service.delete_heuristic_interaction(interaction, timespan)

            # TODO: Move it to heuristics.
            # Wipes the scoreboard every 24 hours.
            if (dateutils.temporal(datetime.now())[:-3] == '21:00'):
                # Gets the winner of every server.
                for guild in self.client.guilds:

                    # Finds the bound channel for announcement or continues the loop if there is none.
                    channel = binding_service.find_bound_channel(guild.id)
                    if not channel: continue

                    # Fetches the channel to announce.
                    channel = self.client.get_channel(channel.channel)

                    # Finds the top score of this server or continue if there is none.
                    score = scoreboard_service.find_top_score(guild.id)
                    if not score: continue

                    # Amount of gold won.
                    amount = random.randint(1000, 1500)

                    # Announces on this server.
                    user_fetch = self.client.get_user(score.user)
                    response = await reader.read('events/ready', 'scoreboard', user_fetch.display_name, score.value, score.unit, amount)

                    # Adds money to the user.
                    user_service.edit_gold(user_fetch.id, guild.id, amount)

                    await channel.send(response)
                    
                # Clears the scoreboard.
                scoreboard_service.truncate_scoreboard()
            
            await asyncio.sleep(timer)
    
    async def heuristics(self, timer):
        '''Checks for heuristics events (ie birthday and character bid of the day).'''
        while True:
            # Birthday to announce at this time.
            if (dateutils.temporal(datetime.now())[:-3] == '09:00'):
                # Find users with birthday not null for each server and date of today.
                for guild in self.client.guilds:

                    # Finds the bound channel for announcement or continues the loop if there is none.
                    channel = binding_service.find_bound_channel(guild.id)
                    if not channel: continue

                    # Fetches the channel to announce.
                    channel = self.client.get_channel(channel.channel)

                    # All the birthdays from this server.
                    users = user_service.find_users_having_birthday(guild.id)
                    
                    # Loop through all users having birthday in this server.
                    for user in users:
                        
                        # Fetches the user.
                        user_fetch = self.client.get_user(user.id)
                        
                        if user.display: response = await reader.read('events/ready', 'birthday-age', user_fetch.display_name, dateutils.age(user.date), f'<@{user_fetch.id}>')
                        else: response = await reader.read('events/ready', 'birthday', user_fetch.display_name, f'<@{user_fetch.id}>')
                        
                        await channel.send(response)
            
            await asyncio.sleep(timer)

    async def rss(self, timer):
        '''Checks for rss feed concerning specified topics.'''
        while True:
            url = settings.rss['url']
            
            headers = {
                'Accept-Language' : 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
            }

            try:
                r = requests.get(url, headers = headers)
            except Exception as e:
                print(f' Erreur survenue lors de la récupération de la source : {url}\n {e}')
            
            try:
                soup = BeautifulSoup(r.content, features = "xml")
            except Exception as e:
                print(f' Erreur survenue lors de la récupération des données xml : {url}\n {e}')
            
            items = soup.find_all('item')
            elements = [{'title': item.find('title').text, 'date': item.find('pubDate').text, 'source': item.find('link').text} for item in items]
            
            for e in elements:
                keyword = settings.rss['title']
                now = datetime.now(timezone.utc)
                posted = datetime.strptime(e['date'], '%a, %d %b %Y %H:%M:%S %z')
                
                # Skip this element if it does not meet the requirements.
                if (keyword not in e['title'].lower()) or (now - posted > timedelta(days = 1)): continue
                
                # If this key is not already present in our json file.
                if not writer.json_key_exists(keyword, e['date']):
                    # Adds a new key to the json dictionary and the link as value.
                    writer.json_value_update(keyword, e['date'], e['source'])
                    print('Une nouvelle entrée rss [{title}] a été ajoutée au dictionnaire json.'.format(title = settings.rss['title']))

                    # Communicates this info to the server.
                    channel = self.client.get_channel(577914680282972170)
                    await channel.send(e['source'])

            await asyncio.sleep(timer)
    
    @Cog.listener()
    async def on_ready(self):

        # Shows a classical console alert for loggin in.
        print(f'\n{self.client.user} connecté avec succès.')

        # Logs how many guilds we are connected to.
        print(f'{len(self.client.guilds)} Guilde(s).')

        # Setting the bot's activity (status).
        await self.client.change_presence(status = nextcord.Status.online, activity = nextcord.Activity(name = "les échos des âmes.", type = ActivityType.listening))

        # Periodically.
        await asyncio.gather(self.syncs(60), self.clean(60), self.heuristics(60))

def setup(bot: Client) -> None:
    bot.add_cog(Ready(bot))