from random import *
import Blocks
block_number_x = 10
block_number_y = 10

Map_Tiles_List = [[0 for col in range(block_number_x)] for row in range(block_number_y)]


def add_water(row, col):
    new_Block = Blocks.Water(10000/block_number_x*row, 10000/block_number_x*col)
    Map_Tiles_List[row][col] = new_Block


def add_dirt(row, col):
    new_Block = Blocks.Dirt(10000/block_number_x*row, 10000/block_number_x*col)
    Map_Tiles_List[row][col] = new_Block


def add_rocks(row, col):
    new_Block = Blocks.Rock(10000/block_number_x*row, 10000/block_number_x*col)
    Map_Tiles_List[row][col] = new_Block


def add_grass(row, col):
    new_Block = Blocks.Grass(10000/block_number_x*row, 10000/block_number_x*col)
    Map_Tiles_List[row][col] = new_Block


def create_map():

    for row in range(block_number_y):
        for col in range(block_number_x):
            rand = randint(0, 3)

            if rand == 0:
                add_water(row, col)
            elif rand == 1:
                add_dirt(row, col)
            elif rand == 2:
                add_rocks(row, col)
            elif rand == 3:
                add_grass(row, col)

    for row in range(0, block_number_x):
        for col in range(0, 2):
            add_grass(col, row)

    for row in range(0, block_number_x):
        for col in range(block_number_x - 2, block_number_x):
            add_grass(col, row)




def init():
    create_map()
    print(Map_Tiles_List)










