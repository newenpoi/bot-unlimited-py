import nextcord
from nextcord import Client, Message, RawReactionActionEvent
from nextcord.ext.commands import Cog

from utils import reader
from services import role_service

'''
    Problème :
    Les mentions ne partagent plus le même identifiant dans les canaux privés.
'''

class Reaction(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    @Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent) -> None:
        # We do not want out client to interfere.
        if payload.user_id == self.client.user.id: return

        # Vérifions si cette réaction appartient au message utilisé pour gérer les rôles enregistrés dans la base de données.
        data = role_service.find_role(payload.guild_id, payload.channel_id, payload.message_id, payload.emoji)

        # Si les données correspondent à l'émoji sélectionné.
        if data is not None and (data.emoji == payload.emoji.name or data.emoji == str(payload.emoji)):

            # Fetches the guild to retrieve the role by id.
            guild = await self.client.fetch_guild(payload.guild_id)

            # Retrieves the role by id.
            role = nextcord.utils.get(guild.roles, id = data.id_role)

            # Affecte le rôle spécifié dans les données.
            await payload.member.add_roles(role)

    @Cog.listener()
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent) -> None:
        # We do not want out client to interfere.
        if payload.user_id == self.client.user.id: return

        # Vérifions si cette réaction appartient au message utilisé pour gérer les rôles enregistrés dans la base de données.
        data = role_service.find_role(payload.guild_id, payload.channel_id, payload.message_id, payload.emoji)

        # Si les données correspondent à l'émoji retiré.
        if data is not None and (data.emoji == payload.emoji.name or data.emoji == str(payload.emoji)):
            # TODO: Removing a reaction with a deleted emoji must be handled.

            # Fetches the guild to retrieve the role by id.
            guild = await self.client.fetch_guild(payload.guild_id)

            # Retrieves the role by id.
            role = nextcord.utils.get(guild.roles, id = data.id_role)

            # Fetches user because member from payload only works on reaction add.
            member = await guild.fetch_member(payload.user_id)

            # Affecte le rôle spécifié dans les données.
            await member.remove_roles(role)
        
def setup(bot: Client) -> None:
    bot.add_cog(Reaction(bot))