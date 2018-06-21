from random import *
import math
from map import Map
import loading_screen

class MapGenerator:

    def __init__(self, rows, cols, screen, settings):
        self.ITERATIONS = 10
        self.cols = cols
        self.rows = rows
        self.screen = screen
        self.settings = settings
        self.tiles = Map(rows, cols)
        self.actual_step = 0


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

    def draw_status(self):
        self.load_screen.update(self.actual_step)
        self.load_screen.draw(self.screen)

    def add_flowers(self):
        pass

    def voronoi_texture(self, element_list):

        # random points are indicator for biome:

        point_list = []

        for x in range(randint(int(self.rows*5), int(self.rows*5))):
            point_list.append([randint(0, self.rows-1), randint(0, self.cols-1), choice(element_list)])

        # ---------------------------------
        self.load_screen = loading_screen.LoadingScreen((self.cols * self.rows * len(point_list)), self.settings)


        for col in range(self.cols):
            self.draw_status()
            for row in range(self.rows):
                # get nearest indicator point:

                nearest_distance_point = [99999, 0, 0]  # [distance, col, row]

                for point in point_list:
                    self.actual_step += 1
                    distance = math.hypot(abs(col-point[1]), abs(row-point[0]))
                    """if distance > 550:
                        print(distance)
                        print(abs(row-point[0]), abs(point[1]-col))
                        print(point)
                        print(row, col)"""

                    if distance < nearest_distance_point[0]:
                        nearest_distance_point = [distance, point[0], point[1], point[2]]

                #print(nearest_distance_point)
                #print(row, col)
                self.tiles.set_field(row, col, nearest_distance_point[3])

    def land_masses(self):
        count = self.ITERATIONS
        for i in range(count):
            self.actual_step = i
            self.draw_status()
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


def create_map(rows, cols, screen, settings):
    seed_num = randint(0, 999999)
    print("seed: ", seed_num)
    seed(seed_num)

    g = MapGenerator(rows, cols, screen, settings)
    grass_chance_list = grass_chance()
    g.random(grass_chance_list)
    #g.land_masses()
    g.voronoi_texture(grass_chance_list)
    g.add_grass_stripes()
    return g.tiles


def init(rows, cols, screen, settings):
    map = create_map(rows, cols, screen, settings)
    print(map.text())
    return map


def grass_chance():
    liste = []

    grass = 0.2
    rock = 0.1
    water = 0.0
    dirt = 0.1

    for p in range(int(50*grass)):
        liste.append(0)
    for c in range(int(50*rock)):
        liste.append(3)
    for t in range(int(50*water)):
        liste.append(1)
    for k in range(int(50*dirt)):
        liste.append(2)

    return liste









