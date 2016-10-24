'''
Written on 10-23-2016 by Nathaniel Green

A direction Enum class for a CornMaze game

'''


from enum import Enum
from random import choice


class Direction(Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3


    def randomDirection():
        return choice(list(Direction))
