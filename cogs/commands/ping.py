from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import reader

class Ping(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "ping", description = "Renvoie ma latence.", guild_ids = [535877732106764288])
    async def ping(self, interaction: Interaction) -> None:
        # Peut être également réalisé avec le formattage (:.2f).
        response = await reader.read('commands/ping', 'latency', round(self.bot.latency * 1000))
        await interaction.send(response)

def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))