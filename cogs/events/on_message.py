import nextcord

from nextcord import Client, Interaction, Message
from nextcord.ext.commands import Cog

class Message(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    @Cog.listener()
    async def on_message(self, message: nextcord.Message) -> None:
        if message.author == self.client.user: return
        await message.channel.send(f"Interception du message : {message.content}")
        
def setup(bot: Client) -> None:
    bot.add_cog(Message(bot))