import random

from nextcord import Embed, Interaction, Member, SlashOption, slash_command
from nextcord.ext.commands import Bot, Cog
from pony.orm import *
from utils import reader
from services import user_service, interaction_service

# TODO : Ajuster automatiquement l'extension vers gif côté serveur (voir htaccess ou vshosts).

class Lift(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "soulever", description = "Soulève la personne mentionnée.", guild_ids = [535877732106764288])
    async def lift(self, interaction: Interaction, member: Member = SlashOption(required = True, description = "Qui souhaites-tu soulever ?")) -> None:

        # La réponse initiale est définie sur None.
        response = None
        
        # On a soulevé moins de x personnes (TODO : Options).
        n = interaction_service.find_user_interaction_count(interaction.user.id, interaction.guild.id, 'soulever')
        if (n >= 3): response = await reader.read('commands/lift', 'max')
        
        # On a assez de vitalité pour soulever la personne.
        health = user_service.find_health(interaction.user.id, interaction.guild.id)
        if (health <= 0): response = await reader.read('commands/lift', 'vitality', member.display_name)
        
        # La cible doit avoir assez de vitalité pour être soulevée (ne doit pas être ko).
        health = user_service.find_health(member.id, interaction.guild.id)
        if (health <= 0): response = await reader.read('commands/lift', 'ko', member.display_name)

        # Selon la condition de response.
        if (response): await interaction.send(response)
        else:
            # On tire un nombre au hasard entre zéro et neuf.
            health = random.randint(0, 14)

            # On ajuste les points de vie de la cible.
            user_service.edit_health(member.id, interaction.guild.id, -health)

            # On ajoute une interaction supplémentaire.
            interaction_service.add_interaction(interaction.user.id, interaction.guild.id, 'soulever')
            
            if (health > 0): response = await reader.read('commands/lift', 'lifted', interaction.user.display_name, member.display_name, health)
            else: response = await reader.read('commands/lift', 'none', member.display_name)

            # Embed.
            embed = Embed(title = 'Bagarre !', description = response, color = 0xe8705a)
            embed.set_image(url = f"http://18.168.128.213/img/hatada/lift/0{(random.randint(1, 6) if health > 0 else 0)}.gif")

            await interaction.send(embed = embed)

    @lift.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Lift(bot))