'''

Written on 10-23-2016 by Nathaniel Green

A player class for a CornMaze game. A player has a
name, an amount of bullets left to shoot, and a location
on the map in the form of a node it is attached to

'''


from direction import Direction as Direct
from random import choice


class Player:
    
    def __init__(self,name):
        self.bullets = 2
        self.location = None
        self.name = name

    # a bullet travels until it hits a player (including the shooter)
    # or a wall, in which case it stops
    def shoot(self,direction):
        node = self.location
        while node.getNeighbor(direction):
            node = node.getNeighbor(direction)
            if node.hasPlayer():
                thePlayer = node.getPlayer()
                thePlayer.die()

    # when a player dies
    def die(self):
        print("Player: {} has died!".format(self.name))


    # All move functions will need to be updated for nodes hosting multiple players
    def moveUp(self):
        if not self.location.top:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.top
        self.location.player = self
        return True

    def moveDown(self):
        if not self.location.bottom:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.bottom
        self.location.player = self
        return True
        
    def moveLeft(self):
        if not self.location.left:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.left
        self.location.player = self
        return True
        
    def moveRight(self):
        if not self.location.right:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.right
        self.location.player = self
        return True


def printFail():
    print("The way is obstructed in this direction")


def getRandomName():
    return choice(["Abby","Brandon","Carla","Dale","Ellen","Frederick","Gale","Harry","Ira"])
