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
                player = node.getPlayer():
                player.die()
    
    def die(self):
        print("Player: {} has died!".format(self.name))


    # All move functions will need to be updated for nodes hosting multiple players
    def moveUp(self):
        if not self.location.up:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.up
        self.location.player = player

    def moveDown(self):
        if not self.location.down:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.down
        self.location.player = player

    def moveLeft(self):
        if not self.location.left:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.left
        self.location.player = player

    def moveRight(self):
        if not self.location.right:
            printFail()
            return False
        self.location.player = None
        self.location = self.location.right
        self.location.player = player



def printFail():
    print("The was is obstructed in this direction")


def getRandomName():
    return choice(["Abby","Brandon","Carlie","Dale","Ellen","Frederick"])
