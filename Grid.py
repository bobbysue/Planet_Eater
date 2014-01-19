import random

class Grid:
    def __init__(self, rows, cols):
        self.grid = []
        for i in range(0, rows):
            self.grid.append([])
            for j in range(0, cols):
                self.grid[i].append(Hex())
    def getType(self, row, col):
        return self.grid[row][col].getType()



class Hex:
    def __init__(self):
        self.type = (int) (random.random() * 5)
        self.explored = False
    def getType(self):
        return self.type

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

