from typing import Union
import re

def nest(d):
    """Converti un dictionnaire en une structure imbriquée (un objet de Structure)."""
    if isinstance(d, list):
        d = [nest(x) for x in d]
    if not isinstance(d, dict):
        return d
    class Structure(object):
        pass
    objet = Structure()
    for k in d:
        objet.__dict__[k.lower()] = nest(d[k])
    return objet

def sort(input: Union[int, str]):
    """Tri les entiers en séparant les milliers."""
    return re.sub(r'\B(\-)?(?=(?:\d{3})+(?:\.|$))', ' ', str(input))

def raritycolor(rarity: int):
    """
        Renvoie la couleur appropriée selon la rareté.
        TODO: Se baser sur un dictionnaire (priorité faible car nécessite de tronquer la requête sql des accesseurs).
    """
    rarities = [0xBADAD1, 0x98FB98, 0x96F7FE, 0xFFFA95, 0xAD64FF]

    return rarities[rarity - 1]

def concat(items: list, prototype: str):
    """Concatène les éléments de manière propre et stylé."""
    string = ""
    
    if prototype == 'inventory':
        for item in items:
            # Tronquage.
            augmented = f"+{item.augmented}" if item.augmented else ''
            name = f'{item.quantity} {item.item_label[:15]} {augmented}'
            locked = "Oui" if item.islocked else "Non"
            
            string += "{:<8} {:<20} {:<12} {:<12} {:<4}\n".format(concat(item.id), name, item.rarity_label, item.item_value, locked)
    
    if prototype == 'quiz':
        for item in items:
            # Tronquage.
            name = f'{item.user_id_unique[:15]}'
            score = f"+{item.score}" if item.score >= 0 else f'-{item.score}'
            
            string += "{:<18} {:<12}\n".format(name, score)
    
    return string