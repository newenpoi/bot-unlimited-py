from nextcord import Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from services import user_service, pull_service, waifu_service
from utils import reader, dateutils

class Claim(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "claim", description = "Permet de s'approprier une waifu qui a été pull précédemment.", guild_ids = [535877732106764288])
    async def claim(self, interaction: Interaction) -> None:
        
        # La réponse initiale est définie sur None.
        response = None
        
        # On doit récupérer le dernier pull.
        pull = pull_service.find_pull(interaction.user.id, interaction.guild.id)
        if not pull: response = await reader.read('commands/claim', 'none')

        # Si le dernier pull est périmé (ou temps négatif).
        if dateutils.elapsed(pull.created) > 300 or dateutils.elapsed(pull.created) < 0: response = await reader.read('commands/claim', 'timeout', interaction.user.display_name)

        # Si on possède déjà cette waifu.
        if waifu_service.find_waifu(interaction.user.id, interaction.guild_id, pull.waifu.id): response = await reader.read('commands/claim', 'exist')

        # On doit avoir assez de crédits.
        if user_service.find_gold(interaction.user.id, interaction.guild_id) < pull.waifu.price: response = await reader.read('commands/claim', 'fund')

        if not response:
            # Ajout de cette waifu à l'utilisateur.
            waifu_service.add_user_waifu(interaction.user.id, interaction.guild_id, pull.waifu.id)

            # Retrait des sommes d'argent.
            user_service.edit_gold(interaction.user.id, interaction.guild_id, -pull.waifu.price)

            # Annonce.
            response = await reader.read('commands/claim', 'claimed', interaction.user.display_name, pull.waifu.name, pull.waifu.price)
        
        await interaction.send(response)

    @claim.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Claim(bot))