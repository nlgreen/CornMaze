'''
Written on 10-19-2016 by Nathaniel Green

A Node class for a CornMaze game. Every Node has a top,
bottom, left, and right that will be other None in the case
of a wall and a Node if there is a connection. Nodes are
valid if they are accessible on the map. Nodes may or may
not have a player attached to them.

TODO: Input checking

'''

from direction import Direction as Direct

class Node:
    def __init__(self):

        # list of nodes this node is connected to
        self.top = None
        self.bottom = None
        self.right = None
        self.left = None

        # used in checking that the node can be accessed
        self.valid = False

        # A node might have a player attached to it
        self.player = None

        self.p1visit = False
        self.p2visit = False
    
    def __str__(self):
        return "Node"

    # attach a node to another node in a specified
    # direction
    def setNode(self, setNumber, node):
        if setNumber == Direct.TOP:
            self.top = node
            node.bottom = self
        elif setNumber == Direct.BOTTOM:
            self.bottom = node
            node.top = self
        elif setNumber == Direct.LEFT:
            self.left = node
            node.right = self
        elif setNumber == Direct.RIGHT:
            self.right = node
            node.left = self

        else:
            print("Incorrect set number")


    # retrieve just one neighbor in a specified direction
    def getNeighbor(self,direction):
        if direction == Direct.TOP:
            return self.top
        elif direction == Direct.BOTTOM:
            return self.bottom
        elif direction == Direct.LEFT:
            return self.left
        elif direction == Direct.RIGHT:
            return self.right


    # retrieve all neighbors in a list
    def getNeighbors(self):
        neighbors = []

        if self.top:
            neighbors.append(self.top)
        if self.bottom:
            neighbors.append(self.bottom)
        if self.left:
            neighbors.append(self.left)
        if self.right:
            neighbors.append(self.right)

        return neighbors
        
    def setVisited(self,thePlayer):
        if thePlayer.number == 1:
            self.p1visit = True
        else:
            self.p2visit = True

    def hasVisited(self,thePlayer):
        if thePlayer.number == 1:
            return self.p1visit
        else:
            return self.p2visit
    

    def hasPlayer(self):
        return bool(self.player)

    def getPlayer(self):
        return self.player

    # attach a player to this node
    def addPlayer(self,thePlayer):
        self.player = thePlayer

    
