from nextcord import Interaction, slash_command, SlashOption, Member, Embed
from nextcord.ext.commands import Bot, Cog
from services import interaction_service
from utils import helper, reader

class Warn(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "warn", description = "Avertir l'utilisateur cible (ex : comportement indésirable).", guild_ids = [535877732106764288], default_member_permissions = 8)
    async def warn(self, interaction: Interaction, 
        target: Member = SlashOption(required = True, description = "La cible à avertir."),
        reason: int = SlashOption(required = True, description = "Choisir la raison de l'avertissement.", choices = {"Comportement Perturbateur": 0, "Parfaitement Incompétent": 1, "Blasphème": 2, "Manque de Respect": 3})
    ) -> None:

        # Ajoute un avertissement pour cet utilisateur dans les interactions (warn).
        interaction_service.add_interaction(target.id, interaction.guild_id, 'warn')

        # Embed a renvoyer au serveur.
        embed = Embed(title = "\💀・Avertissement", description = await reader.read('commands/warn', reason, target.display_name), color = helper.raritycolor(4))
        
        await interaction.send(embed = embed)

    @warn.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Warn(bot))