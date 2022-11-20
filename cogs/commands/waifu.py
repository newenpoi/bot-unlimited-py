from nextcord import Embed, Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from services import interaction_service, pull_service
from utils import reader

class Waifu(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "waifu", description = "Cette commande fait appel à une waifu qui peut être claim.", guild_ids = [535877732106764288])
    async def waifu(self, interaction: Interaction) -> None:
        
        # La réponse initiale est définie sur None.
        response = None
        
        # On a exécuté cette commande trois fois dans un délai spécifié (TODO : Options).
        n = interaction_service.find_user_interaction_count(interaction.user.id, interaction.guild.id, 'waifu')
        if (n >= 3): response = await reader.read('commands/waifu', 'max')

        # TODO : Renvoyer les données de la requête.

        # Instancie un pull de waifu aléatoire.
        pull_service.add_user_pull(interaction.user.id, interaction.guild.id)

        # Récupère la waifu instanciée.
        pull = pull_service.find_pull(interaction.user.id, interaction.guild.id)

        # On ajoute une interaction supplémentaire.
        interaction_service.add_interaction(interaction.user.id, interaction.guild.id, 'waifu')

        # Selon la condition de response.
        if (response): await interaction.send(response)
        else:
            # Embed.
            embed = Embed(title = f"\📑 {pull.waifu.name}", description = "Utilise /claim si tu veux t'approprier ce personnage.", color = (0x4287f5 if pull.waifu.gender == 'M' else 0xdf64f5))
            embed.set_image(url = pull.url)

            embed.add_field(name = "Prix", value = f'```💰 {pull.waifu.price}```')
            embed.add_field(name = "Origine", value = f'```🌍 {pull.waifu.origin}```', inline = False)

            embed.set_footer(text = (pull.waifu.source or 'Image de source inconnue.'), icon_url = "http://18.168.128.213/img/hatada/icons/pixiv.png")

            await interaction.send(embed = embed)

    @waifu.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Waifu(bot))