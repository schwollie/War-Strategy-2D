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
        self.show_sidebar = True

    def draw_rect(self, screen):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.red, (w-(0.2*w), 0, w-(0.2*w), h))
        pygame.draw.rect(screen, colors.dark_grey, (w - (0.2 * w), 0, w - (0.2 * w), h), int(w/400))

    def create_button(self, arguments = self.change_sidebar_visibilitie()):
        # big rect
        w, h = pygame.display.get_surface().get_size()
        line_strength = int(w/400)
        left = w-(w*0.1)
        top = 0
        width = w-(w*0.1)
        height = h

        self.btn = Button.button(left, top, width, height, "+/-", settings, 1)

    def change_sidebar_visibilitie(self):
        if self.show_sidebar == True:
            self.show_sidebar == False

    def draw_all(self, events):
        self.btn.draw()

        button.check_click_collide(events)

