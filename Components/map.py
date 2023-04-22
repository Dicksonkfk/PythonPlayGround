import random
import pygame as pg
from .. import main

# Map components
MAP_OFFSET_X = 35
MAP_OFFSET_Y = 100
MAP_EMPTY = 0
GRID_X_SIZE = 80
GRID_Y_SIZE = 100


class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]

    def isValid(self, map_x, map_y):
        if (map_x < 0 or map_x >= self.width or
                map_y < 0 or map_y >= self.height):
            return False
        return True

    def isMovable(self, map_x, map_y):
        return (self.map[map_y][map_x] == MAP_EMPTY)

    def getMapIndex(self, x, y):
        x -= MAP_OFFSET_X
        y -= MAP_OFFSET_Y
        return (x // GRID_X_SIZE, y // GRID_Y_SIZE)

    def getMapGridPos(self, map_x, map_y):
        return (map_x * GRID_X_SIZE + GRID_X_SIZE // 2 + MAP_OFFSET_X,
                map_y * GRID_Y_SIZE + GRID_Y_SIZE // 5 * 3 + MAP_OFFSET_Y)

    def setMapGridType(self, map_x, map_y, type):
        self.map[map_y][map_x] = type

    def getRandomMapIndex(self):
        map_x = random.randint(0, self.width - 1)
        map_y = random.randint(0, self.height - 1)
        return (map_x, map_y)

    def showPlant(self, x, y):
        pos = None
        map_x, map_y = self.getMapIndex(x, y)
        if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
            pos = self.getMapGridPos(map_x, map_y)
        return pos

    def showMap(self, mapImg):
        mapImg = pg.image.load('background.jpg')
        main.screen.blit(mapImg, (GRID_X_SIZE, GRID_Y_SIZE))
        return mapImg