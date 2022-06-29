from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import reader

class Bind(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "bind", description = "Permet de me lier à un canal (utilise cette commande dans le canal souhaité).", guild_ids = [535877732106764288], default_member_permissions = 8)
    async def bind(self, interaction: Interaction) -> None:
        
        return False
        await interaction.send(response)

def setup(bot: Bot) -> None:
    bot.add_cog(Bind(bot))