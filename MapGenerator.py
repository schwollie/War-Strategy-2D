import pygame
from random import *
width = 200
height = 200

grass = 0
dirt = 1
rock = 2
water = 3

Map_Tiles_List = [[grass for col in range(width)] for row in range(height)]


def add_water(row, col):
    Map_Tiles_List[row][col] = water


def add_dirt(row, col):
    Map_Tiles_List[row][col] = dirt


def add_rocks(row, col):
    Map_Tiles_List[row][col] = rock


def add_grass(row, col):
    Map_Tiles_List[row][col] = grass


def create_map():
    for row in range(height):
        for col in range(width):
            rand = randint(0, 3)
            print(row, col, "hi")
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









