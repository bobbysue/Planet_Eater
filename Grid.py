import random

class Grid:
    def __init__(self, rows, cols, players):
        self.grid = []
        for i in range(0, rows):
            self.grid.append([])
            for j in range(0, cols):
                self.grid[i].append(Hex())
        players[0].setBaseSquare(Point(0, 0))
        players[1].setBaseSquare(Point(9, 9))
        self.grid[0][0].setType("Base")
        self.grid[9][9].setType("Base")

    def getType(self, row, col):
        return self.grid[row][col].getType()



class Hex:
    def __init__(self):
        self.type = (int) (random.random() * 5)
        self.explored = False
    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def equals(self, p):
        return p.x == self.x and p.y == self.y

