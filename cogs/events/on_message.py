import nextcord

from nextcord import Client, Interaction, Message
from nextcord.ext.commands import Cog

class Message(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    @Cog.listener()
    async def on_message(self, message: nextcord.Message) -> None:
        # Code...
        return False
        
def setup(bot: Client) -> None:
    bot.add_cog(Message(bot))