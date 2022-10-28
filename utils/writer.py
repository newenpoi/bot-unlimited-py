import os
import json
from pathlib import Path

def write(file: str, content: str) -> None:
    with open(file, 'w', encoding = 'utf-8') as f:
        f.write(content)

def json_key_exists(file: str, key: str) -> bool:
    "Vérifie si la clé existe dans le fichier json."
    file = Path(__file__).parents[1] / f"json/rss/{file}.json"

    # Creates file if not exist.
    file.touch(exist_ok = True)

    # Creates empty json dictionary if file is empty.
    if os.path.isfile(file) and os.path.getsize(file) == 0: write(file, '{}')
    
    with open(file, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    if not key in data: return False
    return True

def json_value_update(file: str, key: str, value: str) -> str:
    "Ouvre un fichier json pour y mettre à jour la valeur à la clé spécifiée."

    file = Path(__file__).parents[1] / f"json/rss/{file}.json"
    data = {}
    
    with open(file, 'r', encoding = 'utf-8') as f:
        data = json.load(f)

    # The key is the datetime and value the source.
    data[key] = value

    with open(file, 'w', encoding = 'utf-8') as f:
        json.dump(data, f)