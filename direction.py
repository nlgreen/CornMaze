from enum import Enum
from random import choice


class Direction(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3


    def randomDirection():
        return choice(list(Direction))
