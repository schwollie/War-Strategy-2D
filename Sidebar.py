import pygame
import colors
import Button
import math

Swordsman_image_side = pygame.image.load('images/Swordsman.png')
Bowman_image_side = pygame.image.load('images/Bowman.png')


class Sidebar(pygame.sprite.Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.show_sidebar = True
        self.settings = settings

        self.create_button()

    def change_sidebar_visibility(self):
        if self.show_sidebar:
            self.show_sidebar = False
        else:
            self.show_sidebar = True

    def draw_rect(self, screen):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.red, (w-(0.2*w), 0, w-(0.2*w), h))
        pygame.draw.rect(screen, colors.dark_grey, (w - (0.2 * w), -100, w - (0.2 * w), (h+200)), int(w/50))

    def create_button(self):
        # big rect
        w, h = pygame.display.get_surface().get_size()
        left = w-(w*0.08)
        top = h-(h*0.98)
        width = w*0.05
        height = h*0.05
        self.btn = Button.button(left, top, width, height, "+/-", self.settings, 1, function_to_call=self.change_sidebar_visibility)

    def draw_all(self, screen, events):
        if self.show_sidebar:
            self.draw_rect(screen)

        self.btn.draw_btn(screen)
        if self.btn.check_click_collide(events):
            self.btn.action()



