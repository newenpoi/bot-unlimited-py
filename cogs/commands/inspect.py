import time
from nextcord import Interaction, slash_command, SlashOption, Member, Embed
from nextcord.ext.commands import Bot, Cog
from services import user_service
from utils import dateutils, helper

class Inspect(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "inspect", description = "Affiche les informations de l'utilisateur cible (ou soi-même si aucune mention).", guild_ids = [535877732106764288])
    async def inspect(self, interaction: Interaction, 
        target: Member = SlashOption(required = False, description = "La cible à inspecter.")
    ) -> None:

        # Specifies self if no target.
        if not target: target = interaction.user

        # Les infos sockées en bdd.
        user = user_service.find_user(target.id, interaction.guild_id)

        # Embed à renvoyer.
        embed = Embed(colour = 0x0099FF)
        embed.set_image(url = target.display_avatar.url)

        embed.add_field(name = 'PSEUDO', value = f'```🔥 {target.name}```')
        embed.add_field(name = 'ROUBLES', value = f'```💰 {user.gold}```')
        embed.add_field(name = 'TICK', value = f'```🕥 {helper.sort(dateutils.elapsed(user.tick))}```', inline = False)
        embed.add_field(name = 'VIE', value = f'```❤️ {user.health}```')

        embed.set_footer(text = "Le nombre de tick correspond au nombre de secondes depuis la dernière activité.", icon_url = "http://18.168.128.213/img/hatada/icons/reload.png")

        await interaction.send(embed = embed)

    @inspect.error
    async def error(self, interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Inspect(bot))