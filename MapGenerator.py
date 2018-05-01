import pygame
from random import *
width, height = 200, 200;

grass = 0
dirt = 1
rock = 2
water = 3

Map_Tiles_List = [[grass for x in range(width)] for y in range(height)]


def add_water(x, y):
    print(Map_Tiles_List)
    Map_Tiles_List.insert([x][y], 3)


def add_dirt(x, y):
    Map_Tiles_List.insert([x][y], 1)


def add_rocks(x, y):
    Map_Tiles_List.insert([x][y], 2)


def add_grass(x, y):
    Map_Tiles_List.insert([x][y], 0)


def create_map():
    for x in range(width):
        for y in range(height):
            rand = randint(0, 3)
            if rand == 0:
                add_water(x, y)
            elif rand == 1:
                add_dirt(x, y)
            elif rand == 2:
                add_rocks(x, y)
            elif rand == 3:
                add_grass(x, y)


create_map()

print(Map_Tiles_List)









