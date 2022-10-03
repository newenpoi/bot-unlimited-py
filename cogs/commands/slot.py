import os
import asyncio
from nextcord import Embed, Interaction, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import picture, reader
from services import user_service

class Slot(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "slot", description = "Permet de jouer à la machine à sous et de gagner quelques roubles.", guild_ids = [535877732106764288])
    async def slot(self, interaction: Interaction) -> None:
        # Requires production environment to use this command.
        if (os.sep == "\\"): response = await reader.read('commands/slot', 'production'); return await interaction.send(response)
        
        # Simulates something heavy.
        # async with interaction.channel.typing(): await asyncio.sleep(0.5)

        # The cost for the slot machine is hard coded (100).
        if not user_service.find_gold(interaction.user.id, interaction.guild_id) >= 100: response = await reader.read('commands/slot', 'credit'); return await interaction.send(response)

        # Result and source to the slot machine capture.
        s = picture.slot()

        title = ('Presque !' if s['result'] == 2 else 'Perdu !')
        if s['result'] == 3: title = 'Jackpot !'

        # Possible incomes for to the user.
        if not s['result']: incomes = -100
        elif s['result'] == 2: incomes = 400
        else: incomes = 4000

        if not s['result']: description = f'Tu feras mieux la prochaine fois ! ```diff\n- 💰 100 Roubles```'
        elif s['result'] == 2: description = f'On dirait que ça roule plutôt bien ! ```diff\n+ 💰 {incomes} Roubles```'
        else: description = f'Certains ont vraiment le cul bordé de nouilles ! ```diff\n- 💰 {incomes} Roubles```'

        # Embed.
        embed = Embed(title = title, description = description, color = 0xfcba03)
        embed.set_image(url = s['source'])
        embed.set_footer(text = "Cette commande est en développement.", icon_url = "http://18.168.128.213/img/hatada/icons/reload.png")

        user_service.edit_gold(interaction.user.id, interaction.guild_id, incomes)

        await interaction.send(embed = embed)

def setup(bot: Bot) -> None:
    bot.add_cog(Slot(bot))