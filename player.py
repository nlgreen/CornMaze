from direction import Direction as Direct
from random import choice


class Player:
    
    def __init__(self,name):
        self.bullets = 2
        self.location = None
        self.name = name

    def shoot(self,direction):
        node = self.location
        while node.getNeighbor(direction):
            node = node.getNeighbor(direction)
            if node.hasPlayer():
                thePlayer = node.getPlayer()
                thePlayer.die()
    
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

    def moveDown(self):
        if not self.location.bottom:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.bottom
        self.location.player = self

    def moveLeft(self):
        if not self.location.left:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.left
        self.location.player = self

    def moveRight(self):
        if not self.location.right:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.right
        self.location.player = self



def printFail():
    print("The way is obstructed in this direction")


def getRandomName():
    return choice(["Abby","Brandon","Carlie","Dale","Ellen","Frederick"])
