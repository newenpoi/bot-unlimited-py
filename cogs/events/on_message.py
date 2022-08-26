import nextcord

from nextcord import Client, Interaction, Message
from nextcord.ext.commands import Cog

from utils import reader
from services import interaction_service

class Message(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    @Cog.listener()
    async def on_message(self, message: nextcord.Message) -> None:
        
        # Si on a mentionné notre bot.
        if self.client.user.mentioned_in(message):
            # Récupère le nombre d'interactions de type mention sur ce serveur.
            sum = interaction_service.find_interaction_count(message.guild.id, 'mention')

            if (sum == 4): return
            else: response = reader.interact(sum)

            # Enregistre une interaction supplémentaire.
            interaction_service.add_interaction(message.author.id, message.guild.id, 'mention')
            
            await message.channel.send(response)
        
def setup(bot: Client) -> None:
    bot.add_cog(Message(bot))