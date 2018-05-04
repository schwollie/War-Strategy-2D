import pygame
import MapGenerator


Swordsman_image = pygame.image.load('images/Swordsman.png')
Bowman_image = pygame.image.load('images/Bowman.png')


class Swordsman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Swordsman_image
        self.velocity = 55
        self.health = 60
        self.damage = 60
        self.moral = 75
        self.range = 1


class Bowman(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = Bowman_image
        self.image_side = Bowman_image_side
        self.pos = pos
        self.velocity = 65
        self.health = 20
        self.damage = 20
        self.bow_damage = 40
        self.damage = 20
        self.moral = 60
        self.range = 60



