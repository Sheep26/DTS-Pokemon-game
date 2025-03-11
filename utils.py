import os
from enum import Enum

def clear():
    # Clear the console
    # Windows uses the command cls to clear and linux uses the command clear
    os.system('cls' if os.name == 'nt' else 'clear')

class Status(Enum):
    SUCCESS = 0
    VICTORY = 1
    DEFEAT = 2
    RUN_AWAY = 3
    INVALID_INPUT = 4
    INVALID_POKEMON = 5
    NULL = 6
    QUIT = 7