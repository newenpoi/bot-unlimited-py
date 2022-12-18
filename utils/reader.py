import json
from pathlib import Path
import random
import os
from typing import Union
from pyquery import PyQuery
from typing import Union
from dataclasses import dataclass

@dataclass
class Question:
    title: str
    response: str
    score: int

async def read(path : str, id_tag: str, *args) -> str:
    """
        Lis le contenu de la balise id spécifiée d'un fichier HTML.\n
        Les arguments sont passés via *args pour le formatage.
    """

    root = Path(__file__).parents[1]
    file = root / f"strings/{path}.html"

    with open(file, 'r', encoding = 'utf-8') as wrapper:
        q = PyQuery(wrapper.read())
        element = q(f'div#{id_tag}')
        return element.text(squash_space = False).format(*args)

async def rand(path : str, class_tag: str, *args):
    """Lis le fichier HTML avec la classe spécifiée et renvoie une réponse aléatoire."""
    
    root = Path(__file__).parents[1]
    file = root / f"strings/{path}.html"
    
    with open(file, 'r', encoding = 'utf-8') as file:
        query = PyQuery(file.read())
        
        # Récupère le nombre de blocs contenant la classe spécifiée.
        length = len(query(f'div.{class_tag}'))
        r = random.randint(0, length - 1)
        
        # Sélectionne un bloc random.
        tag = query(f'div.{class_tag}').eq(r)

        if tag == "": print(" Il semblerait que la requête renvoie un résultat vide")

        if tag is None: return f"Je ne trouve pas la réplique __{tag}__ avec pour entier __{r}__ et dont la ligne est __{class_tag}__\nLe délimiteur est défini sur __{length}__ pour cette interaction."
        
        return tag.text(squash_space = False).format(*args)

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

def pick(theme: str = "mixed") -> Union[Question, None]:
    '''
        Récupère un nombre de questions sur un fichier json (quiz).\n
        Prends n'importe quelle question au hasard si aucun theme n'est spécifié.
    '''

    root = Path(__file__).parents[1]
    file = root / f"json/quiz/{theme}.json"
    
    if not os.path.isfile(file): return None

    with open(file, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    identifier, question = random.choice(list(data.items()))

    result = Question(title = question['Q'], response = question['R'], score = question['S'])
    return result