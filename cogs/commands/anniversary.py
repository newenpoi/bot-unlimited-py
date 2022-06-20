from nextcord import Interaction, slash_command, SlashOption
from nextcord.ext.commands import Bot, Cog
from utils import reader

class Anniversary(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "anniv", description = "Permet de définir la date de ton anniversaire et de profiter de pleins de surprises.", guild_ids = [535877732106764288])
    async def anniversary(self, interaction: Interaction, 
        date: str = SlashOption(required = True, description = "La date de ton anniversaire au format JJ/MM/AAAA."),
        show_age: int = SlashOption(required = True, description = "Partager ton âge avec les autres membres du serveur ?", choices = {"Oui" : 1, "Non" : 0})
    ) -> None:
        
        # Vérifier que la date d'anniversaire soit bien valide.

        response = await reader.read('commands/anniversary', 'set', date)
        await interaction.send(response, ephemeral = True)

def setup(bot: Bot) -> None:
    bot.add_cog(Anniversary(bot))