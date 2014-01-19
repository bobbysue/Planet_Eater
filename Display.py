#/usr/bin/env python

import os, pygame, math, operator
from pygame.locals import *
from Game import Game

# This is the rectangular size of the hexagon tiles.
TILE_WIDTH = 52
TILE_HEIGHT = 60

# This is the distance in height between two rows.
ROW_HEIGHT = 46

# This value will be applied to all odd rows x value.
ODD_ROW_X_MOD = 26

def distance(coord1, coord2):
    return math.sqrt( (coord1[0] - coord2[0]) ** 2 + 
                      (coord1[1] - coord2[1]) ** 2)

class Display:
    

    cursorArea = "none"
    selectedHex = (-1, -1)

    def hexMapToPixel(self, mapX, mapY, loc = 'corner'):
        """
        Returns the top left pixel location of a hexagon map location.
        """

        pixelY = mapY * ROW_HEIGHT
        if mapY & 1:
            # Odd rows will be moved to the right.
            pixelX = mapX * TILE_WIDTH + ODD_ROW_X_MOD
        else:
            pixelX = mapX * TILE_WIDTH

        if loc == 'center':
            return (pixelX + TILE_WIDTH/2, pixelY + TILE_HEIGHT/2)
        else:
            return (pixelX, pixelY)

    def pixelToHexMap(self, pixelX, pixelY):
        """
        Returns hex map location of a pixel
        """
        
        mapYGuess = (pixelY - TILE_HEIGHT/2) / ROW_HEIGHT
        if mapYGuess & 1:
            mapXGuess = (pixelX - ODD_ROW_X_MOD - TILE_WIDTH/2) / \
                        TILE_WIDTH
        else:
            mapXGuess = (pixelX - TILE_WIDTH/2) / TILE_WIDTH

        canCent = []

        canCent.append(self.hexMapToPixel(mapXGuess, mapYGuess, 'center'))
        canCent.append(self.hexMapToPixel(mapXGuess+1, mapYGuess, 'center'))
        if mapYGuess & 1:
            canCent.append(self.hexMapToPixel(mapXGuess+1, mapYGuess+1, 
                                              'center'))
        else:
            canCent.append(self.hexMapToPixel(mapXGuess, mapYGuess+1, 
                                              'center'))
            

        canDist = [];

        for i in range(3):
            canDist.append(distance(canCent[i], (pixelX, pixelY)))
        
        minInd = canDist.index(min(canDist))

        return (mapXGuess + minInd % 2 + (minInd / 2) * (mapYGuess & 1), 
               mapYGuess + minInd / 2)

    def drawMap(self):
        """
        Draw the tiles.
        """
        fnt = pygame.font.Font(pygame.font.get_default_font(), 12)

        self.mapimg = pygame.Surface((self.mapWidth, self.mapHeight), 1)
        self.mapimg = self.mapimg.convert()
        self.mapimg.fill((104, 104, 104))

        for x in range(self.game.grid.getCols()):
            for y in range(self.game.grid.getRows()):
                # Get the top left location of the tile.
                pixelX, pixelY = self.hexMapToPixel(x, y)

                # Blit the tile to the map image.
                self.mapimg.blit(self.tiles["dark"], (pixelX, pixelY))
                
                # Mark bases
                if self.game.grid.getType(x, y) == "Base":
                    self.mapimg.blit(self.tiles["base0"], (pixelX, pixelY))
        
    def loadTiles(self):
        """
        Load the tile types
        """
        
        self.tiles = {}

        self.tiles["base0"] = pygame.image.load(
                                    "./images/medRed.png").convert()
        self.tiles["base0"].set_colorkey((0x80, 0x00, 0x80), RLEACCEL)

        self.tiles["dark"] = pygame.image.load( 
                                     "./images/medTile.png").convert()
        self.tiles["dark"].set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
        
        self.tiles["cursor"] = pygame.image.load(
                                   "./images/medCursor.png").convert()
        self.tiles["cursor"].set_colorkey((0x80, 0x00, 0x80), RLEACCEL)
        
        self.cursorPos = self.tiles["cursor"].get_rect()

    def init(self):
        """
        Set up the screen
        """

        self.game = Game()
        
        self.mapWidth = TILE_WIDTH * self.game.grid.getCols() +\
                        ODD_ROW_X_MOD
        self.mapHeight = ROW_HEIGHT * (self.game.grid.getCols()-1) +\
                         TILE_HEIGHT

        self.screen = pygame.display.set_mode((1040, 1040), 1)

        self.loadTiles()
        self.drawMap()
    
    def setCursor(self, x, y):
        """
        Set the hexagon map cursor
        """

        mapX, mapY = self.pixelToHexMap(x, y)
        if mapX in range(self.game.grid.getCols()) and \
                mapY in range(self.game.grid.getRows()):
            pixelX, pixelY = self.hexMapToPixel(mapX, mapY)
            self.cursorPos.topleft = (pixelX, pixelY)
            self.selectedHex = (mapX, mapY)
            self.cursorArea = "map"
        else:
            self.cursorArea = "none"
            self.selectedHex = (-1, -1)

    def drawScreen(self):
        self.screen.blit(self.mapimg, (0, 0))
        if self.cursorArea == "map":
            self.screen.blit(self.tiles["cursor"], self.cursorPos)

        pygame.display.flip()

    def mainLoop(self):
        pygame.init()
        self.init()

        clock = pygame.time.Clock()

        while 1:
            clock.tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == MOUSEMOTION:
                    self.setCursor(event.pos[0], event.pos[1])

            self.drawScreen()
            


def main():
    g = Display()
    g.mainLoop()

if __name__ == '__main__': main()
