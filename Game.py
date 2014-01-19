from Player import *
from Grid import *

class Game:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()

        self.grid = Grid(10, 10)

        self.currentPlayer = self.p1

    def getCols(self, player):
        pass
    
    def getSols(self, player):
        pass
    
    def getHexs(self):
        pass

    def getFarms(self, player):
        pass

    def getWalls(self):
        pass

    def getGates(self):
        pass

    def getResources(self, player):
        pass

    def getBarracks(self, player):
        pass

    def getTurn(self):
        pass

    def getActionLeft(self, unit_row, unit_col):
        pass

    def buildFarm(self, row, col):
        pass

    def move(self, row, col, row2, col2):
        pass

    def explore(self, row, col):
        pass

    def buildBarracks(self, row, col):
        pass

    def destroy(self, row, col):
        pass

    def destroyFence(self, p, p1):
        pass

    def importCol(self):
        pass

    def farm(self, p):
        worked = False
        if(self.currentPlayer.hasDude(p)):
            worked = buildFarm(p)

        if(worked):
            return p
        else:
            return []
            
    

g = Game()
print g.farm(Point(1,1))
