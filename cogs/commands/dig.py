from nextcord import Interaction, slash_command, Embed
from nextcord.ext.commands import Bot, Cog
from utils import reader, helper
from services import item_service, inventory_service

class Dig(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "dig", description = "Creuse dans le but de dénicher des trésors !", guild_ids = [535877732106764288])
    async def dig(self, interaction: Interaction) -> None:
        
        # Just pick a random raw material from the database.
        item = item_service.find_item_by_category_and_random()

        # Make an embed or something (uses item db description or file if not).
        embed = Embed(title = f"\💎・{item.name}", description = (item.description or await reader.read('commands/dig', 'null', item.value, item.rarity, 9)), color = helper.raritycolor(item.rarity_id))
        
        # Adds this item to the user's inventory (note that we only have stackable elements in this command).
        inventory_service.add_user_item(interaction.user.id, interaction.guild_id, item.id, 1, 1)
        
        # Réponse finale.
        await interaction.send(embed = embed)

def setup(bot: Bot) -> None:
    bot.add_cog(Dig(bot))