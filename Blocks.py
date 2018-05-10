import pygame
import Camera

Grass_image = pygame.image.load("images/Grass.jpg")
Dirt_image = pygame.image.load("images/Dirt.jpg")
Water_image = pygame.image.load("images/Water.jpg")
Rock_image = pygame.image.load("images/Rock.jpg")


def load_pics(res):
    global Grass_image
    global Dirt_image
    global Water_image
    global Rock_image

    if res == "high":
        Grass_image = pygame.image.load("images/Grass.jpg").convert()
        Dirt_image = pygame.image.load("images/Dirt.jpg").convert()
        Water_image = pygame.image.load("images/Water.jpg").convert()
        Rock_image = pygame.image.load("images/Rock.jpg").convert()

    if res == "low":
        Grass_image = pygame.image.load("images/low_res/Grass_low_res.jpg").convert()
        Dirt_image = pygame.image.load("images/low_res/Dirt_low_res.jpg").convert()
        Water_image = pygame.image.load("images/low_res/Water_low_res.jpg").convert()
        Rock_image = pygame.image.load("images/low_res/Rock_low_res.jpg").convert()


def resize_pics(new_width, new_height):
    global Grass_image
    global Dirt_image
    global Water_image
    global Rock_image
    if Camera.Camera_pos[2] > 5000:
        load_pics("low")
    else:
        load_pics("high")

    Grass_image = transform_pic(Grass_image, new_width, new_height)
    Dirt_image = transform_pic(Dirt_image, new_width, new_height)
    Water_image = transform_pic(Water_image, new_width, new_height)
    Rock_image = transform_pic(Rock_image, new_width, new_height)


def transform_pic(pic, width, height):
    return pygame.transform.scale(pic, (int(width), int(height)))


class MapSprite(pygame.sprite.DirtySprite):
    def __init__(self, get_image, pos_x, pos_y):
        pygame.sprite.DirtySprite.__init__(self)
        self.get_image = get_image
        self.image = get_image()
        self.rect = self.image.get_rect()
        self.pos_x = pos_x  # in coordinate system 10000 x 10000
        self.pos_y = pos_y  # in coordinate system 10000 x 10000
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.view_pos_x = 0
        self.view_pos_y = 0

    def draw(self, screen):
        screen.blit(self.image, [self.view_pos_x, self.view_pos_y, self.rect[2], self.rect[3]])

    def update_rect(self):
        self.image = self.get_image()
        self.rect = self.image.get_rect()
        self.rect.left = self.pos_x
        self.rect.top = self.pos_y


class Grass(MapSprite):
    def __init__(self, pos_x, pos_y):
        MapSprite.__init__(self, lambda: Grass_image, pos_x, pos_y)


class Dirt(MapSprite):
    def __init__(self, pos_x, pos_y):
        MapSprite.__init__(self, lambda: Dirt_image, pos_x, pos_y)


class Water(MapSprite):
    def __init__(self, pos_x, pos_y):
        MapSprite.__init__(self, lambda: Water_image, pos_x, pos_y)


class Rock(MapSprite):
    def __init__(self, pos_x, pos_y):
        MapSprite.__init__(self, lambda: Rock_image, pos_x, pos_y)
