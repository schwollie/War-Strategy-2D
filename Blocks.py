import pygame


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.image = "images/Grass.png"
        self.x_pos = pos_x
        self.y_pos = pos_y


class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.image = "images/Dirt.png"
        self.x_pos = pos_x
        self.y_pos = pos_y


class Water(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.image = "images/Water.png"
        self.x_pos = pos_x
        self.y_pos = pos_y


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        self.image = "images/Rock.png"
        self.x_pos = pos_x
        self.y_pos = pos_y


#
