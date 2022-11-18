import nextcord
from nextcord import Interaction, slash_command, SlashOption
from nextcord.ext.commands import Bot, Cog
from utils import reader, dateutils
from services import role_service

class Roles(Cog):
    def __init__(self, bot : Bot) -> None:
        self.bot = bot

    @slash_command(name = "roles", description = "Permet d'attribuer ou de supprimer automatiquement un rôle lors des réactions.", guild_ids = [535877732106764288], default_member_permissions = 8)
    async def anniversary(self, interaction: Interaction, 
        choice: int = SlashOption(required = True, description = "Veux tu que je gère ou que je supprime un rôle dans ma gestion ?", choices = {"Ajouter" : 1, "Supprimer" : 0}),
        id_message: str = SlashOption(required = True, description = "Identifiant du message sur lequel écouter les réactions (clic droit message → identifiant)."),
        role: nextcord.Role = SlashOption(required = True, description = "Indiquer le rôle en question."),
        emoji: str = SlashOption(required = True, description = "Indiquer l'emoji représentant le rôle (ex: ✅ ou tout autre émoji personnalisé).")
    ) -> None:

        # On doit avoir des permissions d'administrateur (déjà spécifié en paramètres décorateurs).
        # if interaction.permissions.administrator = True
        
        # La réponse par défaut (rôle créé).
        response = await reader.read('commands/roles', 'created', role.mention, emoji)

        try: int(id_message)
        except: response = await reader.read('commands/roles', 'integer')
        else:
            # Découvrons si le rôle qu'on souhaite gérer est présent dans notre base de données.
            data = role_service.find_role_globally(interaction.guild_id, interaction.channel_id, role.id)

            # Si nous sommes en mode création.
            if choice == 1:
                # Aucune données sur ce serveur et canal, nous pouvons gérer ce nouveau rôle.
                if data is None:
                    # Cherche le message sur lequel écouter les réactions.
                    message = await interaction.channel.fetch_message(id_message)

                    if message is None:
                        # Si le message n'a pas pu être trouvé.
                        response = await reader.read('commands/roles', 'message')
                    else:
                        # Ajout du role à gérer dans la base de données.
                        role_service.add_role(interaction.guild_id, interaction.channel_id, id_message, role.id, emoji)
                else:
                    # Le rôle est déjà géré.
                    response = await reader.read('commands/roles', 'duplicate', role.mention)
            else:
                # Le rôle n'a pas été trouvé et ne peut pas être supprimé.
                if data is None: response = await reader.read('commands/roles', 'not-found')
                else:
                    # Deletes role data from table.
                    role_service.delete_role(role.id)

                    # Role retiré de la gestion.
                    response = await reader.read('commands/roles', 'remove', role.mention)

        await interaction.send(response, ephemeral = True)

def setup(bot: Bot) -> None:
    bot.add_cog(Roles(bot))