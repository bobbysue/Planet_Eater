from random import shuffle

class Player:
    def __init__(self):
        self.resources = { }
        self.resources["Ore"] = 4
        self.resources["Fuel"] = 0
        self.resources["Food"] = 0
        self.resources["Lux"] = 0

        self.farms = [ ]
        self.gates = [ ]
        self.cols = [ ]
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
        self.costMap["Farm"] = ("Ore", 4)
        
    def hasDude(self, p):
        for c in self.cols:
            if(c.equals(p)):
                return True
        for s in self.sols:
            if(s.equals(p)):
                return True
        return False

    def buildFarm(self, p):
        price = costMap["Farm"]
        if(self.resources[price[0]] >= price[1]):
            self.farms.append(p)
            self.resources[price[0]] -= price[1]
            return True
        else:
            return False
