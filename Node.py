'''
Written on 10-19-2016 by Nathaniel Green

A Node class for a CornMaze game. Every Node has a top,
bottom, left, and right that will be other None in the case
of a wall and a Node if there is a connection. Nodes are
valid if they are accessible on the map.

TODO: Input checking

'''

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
        if setNumber == 0:
            self.top = node
            node.bottom = self
        elif setNumber == 1:
            self.bottom = node
            node.top = self
        elif setNumber == 2:
            self.left = node
            node.right = self
        elif setNumber == 3:
            self.right = node
            node.left = self

        else:
            print("Incorrect set number")


    
