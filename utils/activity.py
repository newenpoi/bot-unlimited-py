import enum

class ActivityType(enum.IntEnum):
    """Enumerations for Discord Status."""
    unknown = -1
    playing = 0
    streaming = 1
    listening = 2
    watching = 3