'''
Written 10-20-2016 by Nathaniel Green

A map is a collection of sidelength^2 Nodes

TODO: Input checking
'''

from random import randint
import Node
from tkinter import *

class Map:
    def __init__(self,sidelength=6):
        # All nodes are initialized as None, to be replaced with Nodes
        self.nodelist = [[None for i in range(0,sidelength)] for j in range(0,sidelength)]
        self.sidelength = sidelength

    def __str__(self):
        stringy = ""
        for i in range(0,self.sidelength):
            for j in range(0,self.sidelength):
                stringy += str(self.nodelist[i][j])
                stringy += " "
        return stringy
    
    # Add a node to the map -- returns False if no room left
    def addNode(self,node):
        for i in range(0,self.sidelength):
            for j in range(0,self.sidelength):
                if self.nodelist[i][j] is None:
                    self.nodelist[i][j] = node
                    return True
        return False

    # Create a closed, grid map -- no nodes connect to any others
    def init(self):
        for i in range(self.sidelength * self.sidelength):
            self.addNode(Node.Node())

    # numwalls is number of walls to leave up
    def setWalls(self, numwalls):
        # thus, the amount of walls to remove is the total - the number we want remaining
        # where the total number of walls is 2 * sidelength * sidelength
        # note that top walls are the same walls as bottom walls; same with left/right
        l = self.sidelength
        toRemove = 2 * l * l - numwalls

        # very inefficient -- instead of only selecting possible walls, we guess blindly
        # will take exponentially longer the more we have to remove
        while toRemove != 0:

            i = randint(0,self.sidelength - 1)
            j = randint(0,self.sidelength - 1)


            if(self.removeRandomWall(i,j)):
                toRemove -= 1

    def removeRandomWall(self,i,j):
        direction = randint(0,3)
        
        node = self.nodelist[i][j]
        
        # if the chosen direction is already a node, can't remove the wall there
        # otherwise we add the appropriate node connection
        if direction == 0:
            if node.top:
                return False
            newNode = self.nodelist[(i-1) % self.sidelength][j]
            node.setNode(direction,newNode)
            
        elif direction == 1:
            if node.bottom:
                return False
            newNode = self.nodelist[(i+1) % self.sidelength][j]
            node.setNode(direction,newNode)
                
        elif direction == 2:
            if node.left:
                return False
            newNode = self.nodelist[i][(j-1) % self.sidelength]
            node.setNode(direction,newNode)

        elif direction == 3:
            if node.right:
                return False
            newNode = self.nodelist[i][(j+1) % self.sidelength]
            node.setNode(direction,newNode)

        return True
    

    # Verify that all nodes are accessible on the map
    # If not, remove an offending wall and try again

    # TODO: run this function on all nodes?
    def verify(self):
        self.setInvalid()
        startNode = self.nodelist[0][0]
        startNode.valid = True

        def verifyNode(node):
            for node in node.getNeighbors():
                if node.valid:
                    continue
                node.valid = True
                verifyNode(node)
                
        verifyNode(startNode)

        def freeMap(self):
            for i in range(0,self.sidelength):
                for j in range(0,self.sidelength):
                    print(self.nodelist[i][j].valid)
                    if not self.nodelist[i][j].valid:
                        success = False
                        while not success:
                            success = self.removeRandomWall(i,j)
                        return True
            return False

        if(freeMap(self)):
            self.verify()
                
        
        return

    # Set all nodes to invalid (False) reachable state
    def setInvalid(self):
        for row in self.nodelist:
            for node in row:
                node.valid = False

    # Draw the map in tkinter
    def draw(self):

        master = Tk()

        canvas_width = self.sidelength * 100 + 20
        canvas_height = self.sidelength * 100 + 20

        w = Canvas(master,
                   width = canvas_width,
                   height = canvas_width)
        w.pack()


        height = 10

        # draw walls for each node -- walls technically overlap
        for row in self.nodelist:
            width = 10
            for node in row:
                if not node:
                    continue
                if not node.top:
                    w.create_line(width,height,width+100,height)
                if not node.bottom:
                    w.create_line(width,height+100,width+100,height+100)
                if not node.left:
                    w.create_line(width,height,width,height+100)
                if not node.right:
                    w.create_line(width+100,height,width+100,height+100)
                width += 100
            height += 100

        mainloop()
