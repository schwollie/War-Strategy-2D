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


def land_masses():
    count = 30
    for i in range(count):
        for x in range(0, block_number_x, 1):
            for y in range(0, block_number_y, 1):
                nearby_0_fields = 0
                nearby_2_fields = 0
                nearby_3_fields = 0
                active_block = Map_Tiles_List[y][x]

                for x_2 in range(x-1, x+2):
                    for y_2 in range(y-1, y+2):

                        if x_2 == x and y_2 == y:
                            continue

                        try:
                            active_block == Map_Tiles_List[y_2][x_2]
                        except IndexError:
                            nearby_0_fields += 1

                        try:
                            if Map_Tiles_List[y_2][x_2] == 0:
                                nearby_0_fields += 1
                            elif Map_Tiles_List[y_2][x_2] == 2:
                                nearby_2_fields += 1
                            elif Map_Tiles_List[y_2][x_2] == 3:
                                nearby_3_fields += 1
                        except IndexError:
                            continue

                if nearby_0_fields > 4:
                    Map_Tiles_List[y][x] = 0
                    continue
                elif nearby_3_fields > 4:
                    Map_Tiles_List[y][x] = 3
                    continue
                elif nearby_2_fields > 4:
                    Map_Tiles_List[y][x] = 2
                    continue


def lakes():
    pass


def random(grass_chance):
    for row in range(block_number_x):
        for col in range(block_number_y):
            rand = choice(grass_chance)
            Map_Tiles_List[col][row] = rand


def add_grass_stripes():
    for row in range(0, block_number_x):
        for col in range(0, 5):
            Map_Tiles_List[col][row] = 0

    for row in range(0, block_number_x):
        for col in range(block_number_x-5, block_number_x):
            Map_Tiles_List[col][row] = 0


def grass_chance():
    num = randint(100, 100)
    liste = []

    for i in range(num):
        liste.extend((0, 2, 3))

    liste.extend((0, 2, 3))

    return liste


def create_map():
    seed_num = randint(0, 999999)
    print(seed_num)
    seed(seed_num)

    grass_chance_list = grass_chance()
    random(grass_chance_list)
    land_masses()

    add_grass_stripes()

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


def init():
    create_map()










