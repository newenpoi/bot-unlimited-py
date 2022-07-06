from nextcord import Embed, Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from services import bid_service

class Today(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "today", description = "Affiche la waifu à recruter au moment des enchères.", guild_ids = [535877732106764288])
    async def today(self, interaction: Interaction) -> None:
        # Récupère la waifu actuelle du serveur.
        waifu = bid_service.find_today_bid(interaction.guild_id)

        # Embed.
        embed = Embed(title = waifu.name, description = f'Début des enchères à __19:00__ ! ```💰 {waifu.price}```', color = 0x7c97f7)
        embed.set_image(url = waifu.source)
        embed.set_footer(text = "Image de source inconnue.", icon_url = "http://18.168.128.213/img/hatada/icons/pixiv.png")

        await interaction.send(embed = embed)

def setup(bot: Bot) -> None:
    bot.add_cog(Today(bot))