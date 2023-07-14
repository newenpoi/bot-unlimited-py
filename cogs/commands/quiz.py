import asyncio
from nextcord import Interaction, SlashOption, slash_command
from nextcord.ext.commands import Bot, Cog
from utils import reader, helper
from services import quiz_service, interaction_service, user_service

class Quiz(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "quiz", description = "Démarrer le Quiz pour gagner quelques viagradollars.")
    async def quiz(self, interaction: Interaction, theme: int = SlashOption(required = True, description = "Choisir le thème du Quiz.", choices = {"Mixte": 0})) -> None:
        # Vérifie qu'un quiz n'est pas déjà en cours.
        active = interaction_service.find_interaction_count(interaction.guild_id, 'quiz')

        if active: await interaction.send('Tu te fous de ma gueule ? Un Quiz est déjà en cours.'); return False

        # Ajoute une interaction au serveur.
        interaction_service.add_interaction(interaction.user.id, interaction.guild_id, 'quiz')
        
        # Définir les themes par nom de fichier json.
        themes = ['mixed']; counter = 0

        # Première response pour gérer les interactions.
        message = await interaction.send(f"Quiz sur le thème Mixte.")
        message = await message.fetch()
        
        def check(m):
            if (str(question.response) in m.content) and (m.channel == interaction.channel): return True
            print(f'On dirait que {interaction.user.display_name} a répondu de la merde.')

        while True:
            # Récupère une question parmis celles d'un fichier json.
            question = reader.pick(themes[theme])

            # Envoi la question au serveur.
            await message.reply(question.title)

            # Timeout pour cette question.
            try: msg = await self.bot.wait_for('message', timeout = 10.0, check = check)
            except asyncio.TimeoutError:
                await message.reply(f'La réponse était : {question.response}.')
            else:
                # Le membre a répondu juste à la question.
                congratz = await reader.rand('commands/quiz', 'congratz', msg.author.display_name)
                await msg.reply(congratz)

                # Ajoute une entrée en base de données avec le cumul des points (question.score).
                quiz_service.add_entry(interaction.user.id, interaction.guild_id, question.score)

            counter = counter + 1
            
            # Lorsqu'on peut désormais afficher le résultat.
            if counter >= 10:
                # Récupère les scores des participants.
                result = quiz_service.find_score(interaction.guild_id)

                # Converti user_id_unique en son pseudo discord correspondant.
                for line in result:
                    # Fetches user.
                    user = self.bot.get_user(line.user_id_unique)
                    
                    line.user_id_unique = user.display_name
                    
                    # Ajoute quelques viagradollars au solde de l'utilisateur.
                    user_service.edit_gold(user.id, interaction.guild_id, line.score)

                if len(result) > 0:
                    # Concatène.
                    response = await reader.read('commands/quiz', 'content', helper.concat(result, 'quiz'))
                else:
                    response = "Personne n'a eu de bonnes réponses."

                # Nettoie le score.
                quiz_service.cleanup_score(interaction.guild_id)
                
                # Renvoie une réponse au serveur.
                await message.reply(response)
                break

    @quiz.error
    async def error(self, interaction: Interaction, error):
        await interaction.send(f'```Stack Trace : ${error}```')

def setup(bot: Bot) -> None:
    bot.add_cog(Quiz(bot))