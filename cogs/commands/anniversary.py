import time
from nextcord import Interaction, slash_command, SlashOption
from nextcord.ext.commands import Bot, Cog
from utils import reader, dateutils
from services import user_service, binding_service

class Anniversary(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "anniv", description = "Permet de définir la date de ton anniversaire et de profiter de pleins de surprises.", guild_ids = [535877732106764288])
    async def anniversary(self, interaction: Interaction, 
        date: str = SlashOption(required = True, description = "La date de ton anniversaire au format JJ/MM/AAAA."),
        show_age: int = SlashOption(required = True, description = "Partager ton âge avec les autres membres du serveur ?", choices = {"Oui" : 1, "Non" : 0})
    ) -> None:

        # Verifies if the bot has been bound to a channel.
        binding = binding_service.find_bound_channel(interaction.guild.id)
        if not binding: return await interaction.send("Je ne peux pas gérer cette commande sans être liée à un canal.")

        # Vérifions qu'on ai pas déjà de date de définie.
        birth = user_service.find_birthday(interaction.user.id)
        if birth: response = await reader.read('commands/anniversary', 'defined', birth)
        else:

            # Vérifier que la date d'anniversaire soit bien valide.
            valid = dateutils.valid(date)

            if (not valid): response = await reader.read('commands/anniversary', 'invalid')
            else: response = await reader.read('commands/anniversary', 'set', date)

            # Enregistrer la date en base de données.
            if valid: user_service.edit_birthday(interaction.user.id, interaction.guild_id, date, show_age)

        await interaction.send(response, ephemeral = True)

    @anniversary.error
    async def error(self, interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Anniversary(bot))