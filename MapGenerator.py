import pygame
from random import *
import Blocks
width = 200
height = 200

Grass = Blocks.Grass
Dirt = Blocks.Dirt
Rock = Blocks.Rock
Water = Blocks.Water

Map_Tiles_List = [[0 for col in range(width)] for row in range(height)]


def add_water(row, col):
    Map_Tiles_List[row][col] = Water


def add_dirt(row, col):
    Map_Tiles_List[row][col] = Dirt


def add_rocks(row, col):
    Map_Tiles_List[row][col] = Rock


def add_grass(row, col):
    Map_Tiles_List[row][col] = Grass


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









