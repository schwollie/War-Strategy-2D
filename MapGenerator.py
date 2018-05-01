import pygame
from random import *
import Blocks
width = 200
height = 200

Blocks.Grass = 0
Blocks.Dirt = 1
Blocks.Rock = 2
Blocks.Water = 3

Map_Tiles_List = [[0 for col in range(width)] for row in range(height)]


def add_water(row, col):
    Map_Tiles_List[row][col] = 0


def add_dirt(row, col):
    Map_Tiles_List[row][col] = 1


def add_rocks(row, col):
    Map_Tiles_List[row][col] = 2


def add_grass(row, col):
    Map_Tiles_List[row][col] = 3


def create_map():
    for row in range(height):
        for col in range(width):
            rand = randint(0, 3)
            print(row, col)
            print(Map_Tiles_List[row][col])

            if rand == 0:
                add_water(row, col)
            elif rand == 1:
                add_dirt(row, col)
            elif rand == 2:
                add_rocks(row, col)
            elif rand == 3:
                add_grass(row, col)


create_map()

print(Map_Tiles_List)









