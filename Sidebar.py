import pygame
import colors
#

Swordsman_image_side = pygame.image.load('images/Swordsman.png')
Bowman_image_side = pygame.image.load('images/Bowman.png')


class Sidebar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw_rect(self, screen):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.black, (w-(0.5*w), 0, w-(0.5*w), h))
