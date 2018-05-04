import pygame
import colors
import tkinter
import Button
import math



Swordsman_image_side = pygame.image.load('images/Swordsman.png')
Bowman_image_side = pygame.image.load('images/Bowman.png')


class Sidebar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def draw_rect(self, screen):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.red, (w-(0.2*w), 0, w-(0.2*w), h))
        pygame.draw.rect(screen, colors.dark_grey, (w - (0.2 * w), 0, w - (0.2 * w), h), int(w/400))

    def draw_buttons(self):
        # big rect
        w, h = pygame.display.get_surface().get_size()
        line_strength = int(w/400)
        left = w-(w*0.1)
        top = 0
        width = w-(w*0.1)
        height = h

        btn = Button.button(left, top, width, height, "+", settings, line_strength)
