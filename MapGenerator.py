import pygame
from random import *
width, height = 200, 200;

grass = 0
dirt = 1
rock = 2
water = 3

Map_Tiles_List = [[grass for x in range(width)] for y in range(height)]
print(Map_Tiles_List)

def add_water(x, y):
    Map_Tiles_List.insert([x, y], 3)

def add_dirt(x, y):
    Map_Tiles_List.insert([x, y], 1)

def add_rocks(x, y):
    Map_Tiles_List.insert([x, y], 2)

def add_grass(x, y):
    Map_Tiles_List.insert([x , y], 0)


def create_map():
    for i in Range (width):
        x=random.randint(add_dirt(), add_grass(), add_lake(), add_rocks())
    for a in Range (hight):
        y = random.randint(add_dirt(), add_grass(), add_lake(), add_rocks())


    # wx=randint(0,2)
    # if wx = 1:
    #    Map_Tiles_List.insert(x, 3)
    # else:
    #   Map_Tiles_List.insert(x, 3)








