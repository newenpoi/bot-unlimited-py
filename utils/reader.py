from pathlib import Path
from pyquery import PyQuery

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