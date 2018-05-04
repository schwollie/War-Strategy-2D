import pygame
import colors
#

Swordsman_image_side = pygame.image.load('images/Swordsman.png')
Bowman_image_side = pygame.image.load('images/Bowman.png')


class Sidebar(screen):
    def __init__(self, pos_x, pos_y):
        self.image = image
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.pos_x = x_pos
        self.pos_y = y_pos
        self.screen = screen

    def draw_rect(self):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.black, (w-(0.5*w), h, w-(0.5*w), h))
