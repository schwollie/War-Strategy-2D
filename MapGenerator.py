from random import *
import Blocks
import math

block_number_x = 100
block_number_y = 100

Map_Tiles_List = [[0 for col in range(block_number_x)] for row in range(block_number_y)]


def add_water(row, col):
    new_Block = Blocks.Water(10000/block_number_y*col, 10000 - 10000/block_number_x*row)
    Map_Tiles_List[row][col] = new_Block


def add_dirt(row, col):
    new_Block = Blocks.Dirt(10000/block_number_y*col, 10000 - 10000/block_number_x*row)
    Map_Tiles_List[row][col] = new_Block


def add_rocks(row, col):
    new_Block = Blocks.Rock(10000/block_number_y*col, 10000 - 10000/block_number_x*row)
    Map_Tiles_List[row][col] = new_Block


def add_grass(row, col):
    new_Block = Blocks.Grass(10000/block_number_y*col, 10000 - 10000/block_number_x*row)
    Map_Tiles_List[row][col] = new_Block


def lake():
    number = randint(2, int(block_number_x/22))
    for i in range(0, number):
        print("--------------------")

        start_pos_row = randint(10, block_number_x-10)
        start_pos_col = randint(10, block_number_y - 10)

        max_width = randint(10, 20)
        max_height = randint(max_width-5, max_width+5)

        if start_pos_row + max_width >= block_number_x:
            max_width = block_number_x - start_pos_row
        if start_pos_col + max_height >= block_number_y:
            max_height = block_number_y - start_pos_col

        # fill whole rect

        for row in range(start_pos_row, start_pos_row + max_width):
            for col in range(start_pos_col, start_pos_col+ max_height):
                Map_Tiles_List[col][row] = 1

        # subtract some edges


        mid_point_col = start_pos_col + int(max_height / 2)
        mid_point_row = start_pos_row + int(max_width / 2)

        for row in range(start_pos_row, start_pos_row + max_height):
            for col in range(start_pos_col, start_pos_col + max_width):
                x_distance = abs(mid_point_row - row)
                y_distance = abs(mid_point_col - col)
                distance_mid_point = int(math.sqrt(x_distance**2+y_distance**2))
                del_chance = int(randint(0, distance_mid_point))

                if del_chance > 3:
                    Map_Tiles_List[col][row] = 0


def random():
    for row in range(block_number_x):
        for col in range(block_number_y):
            rand = randint(0, 3)
            Map_Tiles_List[col][row] = rand


def create_map():

    #lake()
    random()

    for row in range(block_number_x):
        for col in range(block_number_y):
            if Map_Tiles_List[row][col] == 0:
                add_grass(row, col)
            elif Map_Tiles_List[row][col] == 1:
                add_water(row, col)
            elif Map_Tiles_List[row][col] == 2:
                add_rocks(row, col)
            elif Map_Tiles_List[row][col] == 3:
                add_dirt(row, col)

    for row in range(0, block_number_x):
        for col in range(0, 5):
            add_grass(col, row)

    for row in range(0, block_number_x):
        for col in range(block_number_x-5, block_number_x):
            add_grass(col, row)



def init():
    create_map()
    print(Map_Tiles_List)










