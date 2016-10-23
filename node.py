'''
Written on 10-19-2016 by Nathaniel Green

A Node class for a CornMaze game. Every Node has a top,
bottom, left, and right that will be other None in the case
of a wall and a Node if there is a connection. Nodes are
valid if they are accessible on the map.

TODO: Input checking

'''

from direction import Direction as Direct

class Node:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.right = None
        self.left = None

        self.valid = False
    
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
        


    