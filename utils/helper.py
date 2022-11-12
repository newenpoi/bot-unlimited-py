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