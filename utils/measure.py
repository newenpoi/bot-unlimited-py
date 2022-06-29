import random
from . import helper

def random_distance():
    units = ["nm", "µm", "mm", "cm", "dm", "m", "ha", "km", "AL (Année Lumière)", "Parsec"]
    unit = random.choice(units); value = random.randint(1, 128)

    # Les valeurs doivent être ajustées pour que la valeur précédente ne dépasse pas la valeur actuelle.
    if unit == 4 and value < 13: value = random.randint(13, 128)
    if unit == 5 and value < 13: value = random.randint(13, 128)
    if unit == 8 and value < 40: value = random.randint(40, 128)

    return helper.nest({'value': value, 'unit': unit, 'scale': units.index(unit)})