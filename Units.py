import pygame


class UnitSwordsmen(pygame.sprite.Sprite):
    def __init__(self, rotation, pos):
        pygame.sprite.Sprite.__init__(self)
        self.rotation = rotation
        self.pos = pos

    def rotate(self, rotation):
        self.rotation = rotation

