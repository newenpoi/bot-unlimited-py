from datetime import date, datetime
import re

def valid(date: str) -> bool:
    # Testing fiability.
    pattern = r"^(0?[1-9]|[12][0-9]|3[01])[/](0?[1-9]|1[012])[/](19[0-9]\d|20[0-1]\d|202[0-1])$"
    if not re.match(pattern, date): return False
    
    # Testing values after we made sure the regex is valid (otherwise index error).
    date = date.split('/'); valid = True; bis = False
    year = int(date[2]); month = int(date[1].lstrip('0')); day = int(date[0].lstrip('0'))

    if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)): bis = True

    if (bis == False and month == 2 and day > 28): valid = False
    elif ((month < 1 or month > 12) or (day < 1 or day > 31)): valid = False
    elif ((month == 4 or month == 6 or month == 9 or month == 11) and (day > 30)): valid = False

    return valid

def temporal(timestamp: datetime) -> str:
    """Returns the time only of a datetime object as a string (ie: '19:15:30')."""
    return datetime.strftime(timestamp, "%H:%M:%S")

def elapsed(timestamp: datetime) -> int:
    """Returns seconds elapsed from a timestamp and now."""
    last = datetime.strptime(str(timestamp), '%Y-%m-%d %H:%M:%S')
    return int((datetime.now() - last).total_seconds())

def age(born: date) -> str:
    """Returns the age with precision based on this date and today."""
    today = datetime.strptime(str(date.today()), '%Y-%m-%d')
    born = datetime.strptime(str(born), '%Y-%m-%d')
    
    # return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return ((today - born).days) / 365