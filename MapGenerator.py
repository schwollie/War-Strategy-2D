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
        self.load_screen = loading_screen.LoadingScreen(self.ITERATIONS, self.settings)
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

    def method_3(self):
        biomes = randint(int(self.cols/4), self.cols/2)
        #biomes = 1

        MIN_RADIUS = 10
        MAX_RADIUS = 25
        BORDER = 1
        for i in range(biomes):
            all_biome_points = set()

            biome_type = choice([Map.DIRT, Map.ROCK, Map.WATER])
            biome_start_point = (randint(BORDER, self.rows-BORDER), randint(BORDER, self.cols-BORDER))
            r_start = randint(MIN_RADIUS, MAX_RADIUS)
            radius_range = [r_start, randint(r_start+randint(2, 10), r_start+randint(10, 20))]

            verticy_list = []
            angle_range = sorted([randint(0, 360) for _ in range(randint(15,25))])
            print(angle_range)

            start_row, start_col = biome_start_point

            for angle_idx in range(len(angle_range)):
                degree = angle_range[angle_idx]
                if angle_idx < len(angle_range)-1:
                    step = angle_range[angle_idx + 1] - degree
                else:
                    step = 360 - degree
                # first point

                #biome_start_point = [self.cols/2, self.rows/2]
                distance_to_start = randint(radius_range[0], radius_range[1])
                #distance_to_start = 10

                delta_row = round(math.sin(math.radians(degree)) * distance_to_start)
                delta_col = round(math.cos(math.radians(degree)) * distance_to_start)

                #print(degree)
                #print(delta_row, delta_col)

                point = (start_row+delta_row, start_col+delta_col)
                verticy_list.append(point)

                # second point for no straight lines:
                distance_to_start_2 = randint(distance_to_start-3, distance_to_start+3)
                delta_row = round(math.sin(math.radians(degree+(step/2))) * distance_to_start_2)
                delta_col = round(math.cos(math.radians(degree+(step/2))) * distance_to_start_2)

                point = (start_row + delta_row, start_col + delta_col)
                verticy_list.append(point)#

                #print(degree+(step/2))
                #print(delta_row, delta_col)

            #"""# ----------------------- # find a line between two points
            temp_verticy_list = []
            for idx in range(0, len(verticy_list)):
                row, col = verticy_list[idx]
                lrow, lcol = verticy_list[idx-1]

                delta_row = row-lrow
                delta_col = col-lcol

                if abs(delta_col) > abs(delta_row):
                    if delta_col == 0:
                        rows_per_col = 0
                    else:
                        rows_per_col = delta_row/delta_col

                    sgn = 1
                    if delta_col < 0:
                        sgn = -1
                    for c in range(int(abs(delta_col))):
                        dc = sgn * c
                        new_point = (round(lrow + (dc*rows_per_col)), lcol+dc)
                        #print(dc, new_point, delta_row, delta_col, rows_per_col)
                        temp_verticy_list.append(new_point)
                        #temp_verticy_list.append([last_point[0], last_point[1]+1, 1])

                else:
                    if delta_row == 0:
                        cols_per_row = 0
                    else:
                        cols_per_row = delta_col/delta_row

                    sgn = 1
                    if delta_row < 0:
                        sgn = -1

                    for r in range(int(abs(delta_row))):
                        dr = sgn * r
                        new_point = (lrow+dr, round(lcol+(dr * cols_per_row)))
                        #print(dr, new_point, delta_row, delta_col, cols_per_row)
                        temp_verticy_list.append(new_point)

            verticy_list.extend(temp_verticy_list)

            #print(len(verticy_list))
            #print(verticy_list)

            #---------------------------- draw edges

            for p in verticy_list:
                all_biome_points.add(p)

            # --------------------------"""  now fill the hole thing
            fill_list = []
            fill_list.append(biome_start_point)
            all_biome_points.add(biome_start_point)
            count = 0

            while fill_list:
                #if count > 100:
                #    break

                point = fill_list.pop(0)
                row, col = point
                #print(count, point)

                offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for offset in offsets:
                    ofr, ofc = offset
                    nr, nc = row + ofr, col + ofc
                    if nc not in range(self.cols) or nr not in range(self.rows):
                        continue
                    np = (nr, nc)
                    if np not in all_biome_points:
                        all_biome_points.add(np)
                        fill_list.append(np)

                count += 1
                #print(len(fill_list))

            for r, c in all_biome_points:
                if c not in range(self.cols) or r not in range(self.rows):
                    continue
                self.tiles.set_field(r, c, biome_type)


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

    def grass(self):
        for y in range(self.cols):
            for x in range(self.rows):
                self.tiles.set_field(x, y, Map.GRASS)


def create_map(rows, cols, screen, settings):
    seed_num = randint(0, 999999)
    print("seed: ", seed_num)
    seed(797319)

    g = MapGenerator(rows, cols, screen, settings)
    grass_chance_list = grass_chance()
    #g.random(grass_chance_list)
    g.grass()
    g.method_3()
    #g.land_masses()
    #g.voronoi_texture(grass_chance_list)
    #g.add_grass_stripes()
    return g.tiles


def init(rows, cols, screen, settings):
    map = create_map(rows, cols, screen, settings)
    #print(map.text())
    return map


def grass_chance():
    liste = []

    grass = 0.1
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


def test():
    map = create_map(1000, 1000, None, None)
    print(map.text())

#test()


