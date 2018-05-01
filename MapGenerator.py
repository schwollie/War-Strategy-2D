import pygame
from random import *
import Blocks
width, height = 200, 200;

grass = 0
dirt = 1
rock = 2
water = 3

Map_Tiles_List = [[grass for x in range(width)] for y in range(height)]
print(Map_Tiles_List)

while True:
    global s
    s=-1
    s = s+1

def add_lake():
    Map_Tiles_List.insert(s, Blocks.Water)

def add_dirt():
    Map_Tiles_List.insert(s, Blocks.Dirt)

def add_rocks():
    Map_Tiles_List.insert(s, Blocks.Rock)

def add_grass():
    Map_Tiles_List.insert(s, Blocks.Grass)


def create_map():
    for i in Range (width[0]):
        x=random.randstr(add_dirt(), add_grass(), add_lake(), add_rocks())
    for a in Range (hight[1]):
        y = random.randstr(add_dirt(), add_grass(), add_lake(), add_rocks())








