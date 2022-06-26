from datetime import datetime

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

def temporal(timestamp: datetime) -> str:
    return datetime.strftime(timestamp, "%H:%M:%S")