from datetime import datetime
import os
import shutil
from pathlib import Path
import random
from PIL import Image, ImageEnhance

def slot() -> dict:
    """Génère une capture d'un simulacre de machine à sous et renvoie le résultat de combinaison."""

    # Default extension handled.
    extension = 'PNG'

    # Array for combinations calculations.
    combinations = []
    
    # Faces for the slot machine.
    root = Path(__file__).parent.parent
    files = os.listdir(f'{root}/assets/faces')

    # Destination.
    destination = root / f'assets/production/{datetime.now().timestamp()}.{extension}'
    production = '/var/www/unlimited/app/public/img/hatada/slot'

    # Retrieves the blueprint to handle (contains nine pictures).
    img = Image.open(f'{root}/assets/slot.png')
    resolution = 40; x = 4; y = 4

    # Must generate a total of 9 pictures for this slot machine.
    for i in range(9):
        
        # Goes to the next line after three faces (adds a little gap).
        if i != 0 and i % 3 == 0:
            x = 4
            y = resolution + y + 4
        
        # Picks up a random face.
        icon = Image.open(f'assets/faces/{random.choice(files)}')
        combinations.append(icon)

        # Reduces brightness except for the center line.
        if i <= 2 or i >= 6:
            if icon.mode != 'RGBA': icon = icon.convert('RGBA')
            else: icon = icon.copy()
            
            alpha = icon.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(0.5)
            icon.putalpha(alpha)
        
        img.paste(icon, (x, y))
        x = x + resolution + 4

    # Sauvegarde
    if not (root / f'assets/production').is_dir(): os.mkdir('assets/production')
    img.save(destination)

    # We must move this picture to the production folder in /var/www/unlimited/app/public/img/hatada/slot
    try: shutil.copyfile(destination, production)
    except: print('Cannot move file from destination to production folder.')

    # Résultats de combinaisons.
    if combinations[3] == combinations[3 + 1] and combinations[3 + 1] == combinations[3 + 2]: return {'result': 3, 'source': production}
    if combinations[3] == combinations[3 + 1] or combinations[3 + 1] == combinations[3 + 2]: return {'result': 2, 'source': production}
    return {'result': 0, 'source': production}
    
if __name__ == '__main__':
    s = slot()
    if s: print(s['result']); print(s['source'])