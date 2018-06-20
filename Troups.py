import pygame
import MapGenerator


Swordsman_image = pygame.image.load('images/Swordsman.png')
Bowman_image = pygame.image.load('images/Bowman.png')

all_troups = []


def load_pics():
    global Swordsman_image
    global Bowman_image
    Swordsman_image = pygame.image.load("images/Swordsman.png")
    Bowman_image = pygame.image.load("images/Bowman.png")


def resize_pics(new_width, new_height):
    global Swordsman_image
    global Bowman_image
    load_pics()
    Swordsman_image = transform_pic(Swordsman_image, new_width, new_height)
    Bowman_image = transform_pic(Bowman_image, new_width, new_height)


def transform_pic(pic, width, height):
    return pygame.transform.scale(pic, (int(width), int(height)))


class Swordsman(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.price = 50
        self.image = Swordsman_image
        self.velocity = 55
        self.health = 60
        self.damage = 60
        self.moral = 75
        self.range = 1

    def draw(self, screen, pos):
        screen.blit(self.image, pos)


class Bowman(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.price = 35
        self.image = Bowman_image
        self.image_side = Bowman_image
        self.pos = pos
        self.velocity = 75
        self.health = 20
        self.damage = 20
        self.bow_damage = 40
        self.damage = 20
        self.moral = 60
        self.range = 60



