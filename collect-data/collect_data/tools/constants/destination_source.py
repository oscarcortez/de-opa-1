from enum import Enum, auto

class DestinationSource(Enum):
    MYSQL = auto()
    POSTGRES = auto()
    SQLITE = auto()
    CSV = auto()
    JSON = auto()