from direction import Direction as Direct

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
