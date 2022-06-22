from nextcord import Client, Interaction, Message
from nextcord.ext.commands import Cog

class Message(Cog):
    def __init__(self, client : Client) -> None:
        self.client = client

    @Cog.listener()
    async def on_message(self, interaction: Interaction) -> None:
        if interaction.message.author == self.client.user: return
        await interaction.message.channel.send(f"Interception du message : {interaction.message.content}")
        
def setup(bot: Client) -> None:
    bot.add_cog(Message(bot))