from random import *
import blocks
from map import Map


class MapGenerator:
    #ITERATIONS = 30
    ITERATIONS = 2

    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows

        self.tiles = Map(rows, cols)

    # def add_water(self, row, col):
    #     new_Block = Blocks.Water(10000/self.rows*col, 10000 - 10000/self.cols*row)
    #     self.tiles[row][col] = new_Block
    #
    #
    # def add_dirt(self, row, col):
    #     new_Block = Blocks.Dirt(10000/self.*col, 10000 - 10000/self.cols*row)
    #     self.tiles[row][col] = new_Block
    #
    #
    # def add_rocks(self, row, col):
    #     new_Block = Blocks.Rock(10000/self.*col, 10000 - 10000/self.cols*row)
    #     self.tiles[row][col] = new_Block
    #
    #
    # def add_grass(self, row, col):
    #     new_Block = Blocks.Grass(10000/self.rows*col, 10000 - 10000/self.cols*row)
    #     self.tiles[row][col] = new_Block

    def land_masses(self):
        count = MapGenerator.ITERATIONS
        for i in range(count):
            print('Pass %d' % i)
            for col in range(self.cols):
                for row in range(self.rows):
                    nearby_0_fields = 0
                    nearby_2_fields = 0
                    nearby_3_fields = 0
                    active_block = self.tiles.get_field(row, col)

                    for col2 in range(col-1, col+2):
                        for row2 in range(row-1, row+2):

                            if col2 == col and row2 == row:
                                continue

                            try:
                                active_block == self.tiles.get_field(row2, col2)
                            except IndexError:
                                nearby_0_fields += 1

                            try:
                                if self.tiles.get_field(row2, col2) == Map.GRASS:
                                    nearby_0_fields += 1
                                elif self.tiles.get_field(row2, col2) == Map.ROCK:
                                    nearby_2_fields += 1
                                elif self.tiles.get_field(row2, col2) == Map.DIRT:
                                    nearby_3_fields += 1
                            except IndexError:
                                continue

                    if nearby_0_fields > 4:
                        self.tiles.set_field(row, col, Map.GRASS)
                        continue
                    elif nearby_3_fields > 4:
                        self.tiles.set_field(row, col, Map.DIRT)
                        continue
                    elif nearby_2_fields > 4:
                        self.tiles.set_field(row, col, Map.ROCK)
                        continue

    def lakes(self):
        pass

    def random(self, grass_chance):
        for row in range(self.cols):
            for col in range(self.rows):
                rand = choice(grass_chance)
                self.tiles.set_field(row, col, rand)

    def add_grass_stripes(self):
        for row in range(self.rows):
            for col in range(0, 2):
                self.tiles.set_field(row, col, Map.GRASS)
                self.tiles.set_field(row, self.cols - col - 1, Map.GRASS)

        for col in range(0, self.cols):
            for row in range(0, 2):
                self.tiles.set_field(row, col, Map.GRASS)
                self.tiles.set_field(self.rows - row - 1, col, Map.GRASS)


        #map = Map(self.rows, self.cols)
        #for row in range(self.rows):
        #    for col in range(self.cols):
        #        if self.tiles[row][col] == 0:
        #            self.add_grass(row, col)
        #        elif self.tiles[row][col] == 1:
        #            self.add_water(row, col)
        #        elif self.tiles[row][col] == 2:
        #            self.add_rocks(row, col)
        #        elif self.tiles[row][col] == 3:
        #            self.add_dirt(row, col)


def create_map(rows, cols):
    seed_num = randint(0, 999999)
    print(seed_num)
    seed(seed_num)

    g = MapGenerator(rows, cols)
    grass_chance_list = grass_chance()
    g.random(grass_chance_list)
    g.land_masses()
    g.add_grass_stripes()
    return g.tiles


def init(rows, cols):
    map = create_map(rows, cols)
    print(map.text())
    return map


def grass_chance():
    num = randint(100, 100)
    liste = []

    for i in range(num):
        liste.extend((0, 2, 3))

    liste.extend((0, 2, 3))

    return liste









