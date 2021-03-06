import math
import pygame
from coord_sys import CoordSys
from map import Map


def transform_pic(pic, width, height):
    return pygame.transform.scale(pic, (int(width), int(height)))


class MapSprite(pygame.sprite.DirtySprite):
    def __init__(self, get_image, name):
        pygame.sprite.DirtySprite.__init__(self)
        self.name = name
        self.get_image = get_image
        self.image = get_image()
        self.rect = self.image.get_rect()

    def draw(self, screen, pos):
        #screen.blit(self.image, [self.view_pos_x, self.view_pos_y, self.rect[2], self.rect[3]])
        screen.blit(self.image, pos)


"""
class Grass(MapSprite):
    def __init__(self):
        MapSprite.__init__(self, lambda: Grass_image, "Grass")


class Dirt(MapSprite):
    def __init__(self):
        MapSprite.__init__(self, lambda: Dirt_image, "Dirt")


class Water(MapSprite):
    def __init__(self):
        MapSprite.__init__(self, lambda: Water_image, "Water")


class Rock(MapSprite):
    def __init__(self):
        MapSprite.__init__(self, lambda: Rock_image, "Rock")
"""


class BlockMap:
    def __init__(self, map):
        self.map = map
        self.load_pics()

    def load_pics(self):
        self.grass = pygame.image.load("images/Grass.jpg").convert()
        self.dirt = pygame.image.load("images/Dirt.jpg").convert()
        self.water = pygame.image.load("images/Water.jpg").convert()
        self.rock = pygame.image.load("images/Rock.jpg").convert()
        self.flowers = pygame.image.load("images/flowers.png").convert_alpha()
        self.tree = pygame.image.load("images/tree.png").convert_alpha()

    def resize_sprites(self, w, h):
        self.grass_sprite = transform_pic(self.grass, w, h)
        self.dirt_sprite = transform_pic(self.dirt, w, h)
        self.water_sprite = transform_pic(self.water, w, h)
        self.rock_sprite = transform_pic(self.rock, w, h)
        self.tree = transform_pic(self.tree, w, h)
        self.flowers = transform_pic(self.flowers, w, h)

    def get_sprites(self, row, col):
        field = self.map.get_field(row, col)
        if field == Map.GRASS: return self.grass_sprite
        if field == Map.WATER: return self.water_sprite
        if field == Map.DIRT: return self.dirt_sprite
        if field == Map.ROCK: return self.rock_sprite
        raise Exception('Unknown field type %d' % field)

    def create_canvas(self, width, height):
        size = max(width, height)
        delta = size / self.map.rows
        block_width = math.ceil(delta)
        block_height = math.ceil(delta)
        self.resize_sprites(block_width, block_height)

        self.coord_sys = CoordSys(pygame.Rect((0,0), (size, size)))
        self.canvas = pygame.Surface((size, size))

        y = 0
        for row in range(self.map.rows):
            x = 0
            for col in range(self.map.cols):
                sprite = self.get_sprites(row, col)
                self.canvas.blit(sprite, (x, y))
                x += delta
            y += delta
        #print("Final size: %s, %s" % (x, y))


    def update(self, width, height):
        width = int(width)
        height = int(height)
        size = max(width, height)
        self.coord_sys = CoordSys(pygame.Rect((0,0), (size, size)))
        self.zoom_canvas = pygame.transform.scale(self.canvas, (size, size))
        #print("Final size: %s, %s" % (x, y))

    def draw(self, screen, view_port):
        screen.blit(self.zoom_canvas, (0, 0), area=view_port)

