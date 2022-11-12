from nextcord import Interaction, slash_command, Embed
from nextcord.ext.commands import Bot, Cog
from utils import reader, helper
from services import item_service, inventory_service, interaction_service

class Dig(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "dig", description = "Creuse dans le but de dénicher des trésors !", guild_ids = [535877732106764288])
    async def dig(self, interaction: Interaction) -> None:
        
        # On a creusé moins de x fois (TODO : Options).
        n = interaction_service.find_user_interaction_count(interaction.user.id, interaction.guild.id, 'dig')
        if (n >= 3): response = await reader.read('commands/dig', 'max'); await interaction.send(response)

        # Sélectionne un matériaux (1) quelconque parmis nos objets.
        item = item_service.find_item_by_category_and_random(1)

        # Make an embed or something (uses item db description or file if not).
        embed = Embed(title = f"\💎・{item.name}", description = (item.description or await reader.read('commands/dig', 'null', item.value, item.rarity.name, (9 - n))), color = helper.raritycolor(item.rarity.id))
        
        # Adds this item to the user's inventory (note that we only have stackable elements in this command).
        inventory_service.add_user_item(interaction.user.id, interaction.guild_id, item.id, 1, 1)

        # On ajoute une interaction supplémentaire.
        interaction_service.add_interaction(interaction.user.id, interaction.guild.id, 'dig')
        
        # Réponse finale.
        await interaction.send(embed = embed)

    @dig.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Dig(bot))