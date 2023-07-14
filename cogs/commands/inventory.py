from nextcord import Interaction, slash_command, Embed
from nextcord.ext.commands import Bot, Cog
from services import user_service, interaction_service
from utils import helper, reader

class Inventory(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "inventory", description = "Cette commande permet d'afficher ton inventaire.", guild_ids = [535877732106764288])
    async def inventory(self, interaction: Interaction) -> None:

        # Sends response to server.
        await interaction.send("Cette commande est en cours de développement.")

    @inventory.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Inventory(bot))