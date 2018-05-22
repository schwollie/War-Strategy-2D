import math
import sys

import pygame

import Button
import Settings
import colors
import ShowMap

global icon
icon = pygame.image.load('images/icon.png')

class Menu(object):
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.screen_caption = pygame.display.set_caption('War Strategy 2D')
        self.screen_icon = pygame.display.set_icon(icon)
        self.btn_list = []
        self.draw_btn_list = []
        pygame.font.init()
        self.create_settings_button(self.settings)
        self.create_start_button(self.settings)
        self.create_load_button(self.settings)
        self.create_battle_button(self.settings)
        self.create_exit_button(self.settings)
        self.create_revert_btn(self.settings)
        self.event = pygame.event.get()

    def draw_buttons(self):
        # big rect
        line_strength = int((math.sqrt(self.settings.resolution[0] * self.settings.resolution[1]) / 400))
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 8)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.2 + self.settings.resolution[1] / 10)
        width = int((self.settings.resolution[0] / 2 + self.settings.resolution[0] / 8) - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 8))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.2) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.2))

        pygame.draw.rect(self.screen, colors.light_grey, [left + line_strength, top + line_strength, width + line_strength, height + line_strength], 0)
        pygame.draw.rect(self.screen, colors.black, [left+line_strength, top+line_strength, width+line_strength, height + line_strength], line_strength)

        self.draw_title()
        for button in self.draw_btn_list:
            button.draw_btn(self.screen)

    def create_start_button(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "Start New Game", settings, 1)
        self.btn_list.append(btn)
        self.draw_btn_list.append(btn)

    def create_load_button(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11 * 2.2)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "Resume Game", settings, 2)
        self.btn_list.append(btn)
        self.draw_btn_list.append(btn)

    def create_battle_button(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11 * 3.5)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "Play Battle", settings, 3, function_to_call=self.start_battle)
        self.btn_list.append(btn)
        self.draw_btn_list.append(btn)

    def create_exit_button(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11 * 6.1)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "EXIT", settings, 4, sys.exit)
        self.btn_list.append(btn)
        self.draw_btn_list.append(btn)

    def create_settings_button(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11 * 4.8)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "Settings", settings, 5, self.start_settings)
        self.btn_list.append(btn)
        self.draw_btn_list.append(btn)

    def draw_title(self):
        pygame.font.init()
        font = pygame.font.Font(None, int(self.settings.resolution_sqrt()/10))
        title = font.render("War Strategy 2D", True, colors.black)
        text_rect = title.get_rect(center=(self.settings.resolution[0] / 2, self.settings.resolution[1] / 6))
        self.screen.blit(title, text_rect)

    def start_settings(self):
        self.settings = Settings.initiate(self.screen, self.settings, self)
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode(self.settings.resolution, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.settings.resolution)

    def create_revert_btn(self, settings):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[
            1] / 11 * 4.8)
        width = settings.resolution[0]
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (
        self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "Accept Settings", settings, 6, self.make_revert_btn_invisible)
        self.btn_list.append(btn)

    def make_revert_btn_invisible(self):
        for btn in self.btn_list:
            if btn.ID == 6:
                self.btn_list.remove(btn)

    def start_battle(self):
        ShowMap.initialize_Map(self.screen, self.settings)

    def process_event(self, events):
        for button in self.btn_list:
            if button.check_click_collide(events):
                button.action()



def show_menu(settings):
    clock = pygame.time.Clock()

    if settings.fullscreen:
        try:
            flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
            screen = pygame.display.set_mode(settings.resolution, flags)
        except pygame.error:
            screen = pygame.display.set_mode((640, 480), flags)
    else:
        try:
            screen = pygame.display.set_mode(settings.resolution, pygame.DOUBLEBUF)
        except pygame.error:
            screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)

    screen.fill(colors.white)

    menu = Menu(settings, screen)

    while True:
        # fps

        # every time a button gets clicked he set this to False to prevent spamming


        clock.tick()

        menu.screen.fill(colors.white)
        menu.draw_buttons()

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            #print(event)
            #print(pygame.mouse.get_pos())

        menu.process_event(events)

        pygame.display.flip()