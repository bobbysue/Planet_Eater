from random import shuffle
from Grid import *

class Player:
    def __init__(self):
        self.resources = { }
        self.resources["Ore"] = 4
        self.resources["Fuel"] = 4
        self.resources["Food"] = 4
        self.resources["Lux"] = 0

        self.farms = [ ]
        self.gates = [ ]
        self.cols = [ Point(1, 1)]
        self.sols = [ ]

        #Things mapping

        things = [ 0, 1, 2, 3, 4]
        shuffle(things)

        self.mapping = { }
        self.mapping["Ore"] = things[0]
        self.mapping["Fuel"] = things[1]
        self.mapping["Lux"] = things[2]
        self.mapping["Food"] = things[3]
        self.mapping["Hab"] = things[4]

        self.costMap = {}
        self.costMap["Farm"] = (("Ore", 4),)
        self.costMap["Colonist"] = (("Fuel", 4), ("Food", 4))

    def checkCost(self, type):
        price = self.costMap[type]
        bool = True
        for p in price:
            print p
            bool = bool and self.resources[p[0]] >= p[1]
        return bool

    def buy(self, type):
        price = self.costMap[type]
        bool = True
        for p in price:
            self.resources[p[0]] -= p[1]
        return bool

    def setBaseSquare(self, p):
        self.base = p

    def importCol(self):
        if(self.base in self.cols):
            return False
        if(self.checkCost("Colonist")):
            self.buy("Colonist")
            self.cols.append(self.base)

    def hasDude(self, p):
        for c in self.cols:
            if(c.equals(p)):
                return True
        for s in self.sols:
            if(s.equals(p)):
                return True
        return False

    def buildFarm(self, p):
        if(self.checkCost("Farm")):
            self.buy("Farm")
            self.farms.append(p)
            return True
        else:
            return False
