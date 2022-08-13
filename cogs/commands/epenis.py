from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import dateutils, reader, measure
from services import interaction_service, scoreboard_service, binding_service

class EPenis(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "epenis", description = "Renvoie la taille de ton e-dps pour aujourd'hui.", guild_ids = [535877732106764288])
    async def epenis(self, interaction: Interaction) -> None:

        # TODO: Make a decorator for bound channel verification.
        # Verifies if the bot has been bound to a channel.
        binding = binding_service.find_bound_channel(interaction.guild.id)
        if not binding: return await interaction.send("Je ne peux pas gérer cette commande sans être liée à un canal.")
        
        # Verifies if we are already in the scoreboard.
        score = scoreboard_service.find_score(interaction.user.id, interaction.guild.id)

        # Finds when we used this command (if there is).
        inter = interaction_service.find_interaction_timestamp(interaction.user.id, interaction.guild.id, 'epenis')
        
        # If there is a score and timestamp or not.
        if (score and inter): response = await reader.read('commands/epenis', 'max', dateutils.temporal(inter.timestamp), score.value, score.unit)
        if (score and not inter):
            # This response will be sent if we cannot get an interaction timestamp signature but still have the score.
            response = await reader.read('commands/epenis', 'basic', score.value, score.unit)

        # Otherwise we can roll the dices.
        if not score:
            # Generates a score.
            size = measure.random_distance()

            # On ajoute une interaction supplémentaire.
            interaction_service.add_interaction(interaction.user.id, interaction.guild.id, 'epenis')

            # Adds the score.
            scoreboard_service.add_score(interaction.user.id, interaction.guild.id, size.value, size.unit, size.scale)
        
            # Gets the response.
            response = await reader.read('commands/epenis', 'result', interaction.user.display_name, size.value, size.unit)
        
        await interaction.send(response)

    @epenis.error
    async def error(self, interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(EPenis(bot))