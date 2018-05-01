from random import *
import Blocks
width = 20
height = 20

Map_Tiles_List = [[0 for col in range(width)] for row in range(height)]


def add_water(row, col):
    new_Block = Blocks.Water(row, col)
    Map_Tiles_List[row][col] = new_Block


def add_dirt(row, col):
    new_Block = Blocks.Dirt(row, col)
    Map_Tiles_List[row][col] = new_Block


def add_rocks(row, col):
    new_Block = Blocks.Rock(row, col)
    Map_Tiles_List[row][col] = new_Block


def add_grass(row, col):
    new_Block = Blocks.Grass(row, col)
    Map_Tiles_List[row][col] = new_Block


def create_map():

    for row in range(height):
        for col in range(width):
            rand = randint(0, 3)
            #print(row, col)
            #print(Map_Tiles_List[row][col])


            if rand == 0:
                add_water(row, col)
            elif rand == 1:
                add_dirt(row, col)
            elif rand == 2:
                add_rocks(row, col)
            elif rand == 3:
                add_grass(row, col)

    for row in range(0, 20):
        for col in range (0, 5):
            add_grass(row, col)

    for row in range(0, 20):
        for col in range (15, 20):
            add_grass(row, col)




def init():
    create_map()
    print(Map_Tiles_List)










