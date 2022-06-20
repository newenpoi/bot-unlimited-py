from attr import s
from nextcord import Embed, Interaction, SlashOption, slash_command
from nextcord.ext.commands import Bot, Cog, ExtensionNotFound
from utils import reader

class Reload(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "reload", description = "Recharge le rouage spécifié.", guild_ids = [535877732106764288], default_member_permissions = 8)
    async def ping(self, interaction: Interaction, extension: str = SlashOption(required = True, description = "Spécifier le rouage à recharger.")) -> None:
        
        # Embed.
        embed = Embed(title = 'Reloaded', description = f"Le rouage avec pour nom d'extension {extension} a été correctement rechargé.", color = 0xdc143c)
        embed.set_image(url = "https://cdn.discordapp.com/attachments/577914680282972170/985120463439155220/96586146_p0_master1200.jpg")

        # Recharge l'extension spécifiée.
        self.bot.reload_extension(f'cogs.commands.{extension}')

        # response = await reader.read('commands/reload', 'reloaded', extension)
        await interaction.send(embed = embed)

    @ping.error
    async def error(self, interaction, error):
        if isinstance(error, ExtensionNotFound): response = await reader.read('commands/reload', 'error'); await interaction.send(response)
        else: await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Reload(bot))