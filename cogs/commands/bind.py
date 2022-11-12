from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import reader
from services import binding_service

class Bind(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "bind", description = "Permet de me lier à un canal (utilise cette commande dans le canal voulu).", guild_ids = [535877732106764288], default_member_permissions = 8)
    async def bind(self, interaction: Interaction) -> None:
        # Calls the service to bind the bot to a channel.
        binding_service.bind_server(interaction.guild_id, interaction.channel_id)

        response = await reader.read('commands/bind', 'bound')
        await interaction.send(response)

    @bind.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Bind(bot))