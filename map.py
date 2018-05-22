import coord_sys
import pygame

class Map:
    GRASS = 0
    WATER = 1
    DIRT = 2
    ROCK = 3

    CHAR = {
        GRASS: '.',
        WATER: '≈',
        DIRT: '*',
        ROCK: '^',
    }

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.map = [[Map.DIRT for _ in range(0, cols)] for _ in range(0, rows)]
        self.coord_sys = coord_sys.CoordSys(pygame.Rect((0, 0), (cols, rows)))

    def set_field(self, row, col, type):
        self.map[row][col] = type

    def get_field(self, row, col):
        return self.map[row][col]

    def get_coord_sys(self):
        return self.coord_sys

    def text(self):
        return '|\n'.join([''.join([Map.CHAR[col] for col in row]) for row in self.map])
