from enum import Enum


class Operations(str, Enum):
    CREATE = "CREATE"
    MOVE = "MOVE"
    DELETE = "DELETE"
    LIST = "LIST"
