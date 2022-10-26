import json
from pathlib import Path
import random
from pyquery import PyQuery
from typing import Union

async def read(path : str, language: str, id_tag: str, *args) -> str:
    """
        Lis le contenu de la balise id spécifiée d'un fichier HTML.\n
        Les arguments sont passés via *args pour le formatage.
    """

    root = Path(__file__).parents[1]
    file = root / f"strings/{path}.{language}.html"

    with open(file, 'r', encoding = 'utf-8') as wrapper:
        q = PyQuery(wrapper.read())
        element = q(f'div#{id_tag}')
        return element.text(squash_space = False).format(*args)

def translate(model: str, code: str, identifier: int) -> str:
    "Récupère la traduction du modèle en fonction du code et de l'identifiant de la ligne."

    root = Path(__file__).parents[1]
    
    # Exemple : json/translation/rarity.json
    file = root / f"json/translation/{model}.json"

    with open(file, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    translation = data[code]

    return translation[str(identifier)]

def conf(field: str, attribute: str):
    "Récupère l'attribut souhaité de la section Système du fichier de configuration.'"

    root = Path(__file__).parents[1]
    file = root / "config/release.ini"

    # Si le fichier de production n'est pas disponible.
    if not file.is_file(): file = root / "config/dev.ini"

    config = configparser.RawConfigParser()
    config.read(file)

    items = {}

    for i in range(len(config.items(field))):
        # {Clé: Valeur} (du fichier ini).
        items.update({config.options(field)[i]: config.get(field, config.options(field)[i])})

    return items[attribute]

def interact(sum: int) -> Union[str, None]:
    "Renvoie une réponse contenue dans le fichier json par rapport à la somme des interactions."
    
    root = Path(__file__).parents[1]
    file = root / f"json/mentions/0{sum}.json"

    with open(file, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    responses = data['response']

    if len(responses): return random.choice(responses)
    else: return None