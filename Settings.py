import pygame
import sys
import colors
import Saved_Settings
import menu
import Button


poss_resolution = [[640, 480], [854, 450], [800, 480], [800, 600], [1024, 768], [1280, 720], [1280, 800], [1440, 900],
                   [1440, 960], [1400, 1050], [1600, 900], [1680, 1050], [1600, 1200], [1920, 1080], [1920, 1200],
                   [2048, 1536], [2560, 1600]]

poss_fullscreen = [True, False]


class ChangeSettings(object):
    def __init__(self, screen, settings, settings_new):
        self.screen = screen
        self.settings = settings
        self.settings_new = settings_new
        self.btn_list = []
        self.create_exit()
        self.create_res()
        self.create_fullscreen()

    def draw_buttons(self):
        for button in self.btn_list:
            button.draw_btn(self.screen)

    def process_event(self, events):
        for button in self.btn_list:
            if button.check_click_collide(events):
                #print(button.ID)
                button.action()

    def change_res(self, direction):
        index = poss_resolution.index(self.settings_new.resolution)
        if direction == "higher":
            index = (index + 1) % len(poss_resolution)
            self.settings_new.resolution = poss_resolution[index]
        if direction == "lower":
            index = (index - 1) % len(poss_resolution)
            self.settings_new.resolution = poss_resolution[index]

    def change_fullscreen(self):
        if self.settings_new.fullscreen:
            self.settings_new.fullscreen = False
        else:
            self.settings_new.fullscreen = True

    def draw_title(self, screen, settings):
        pygame.font.init()
        font = pygame.font.Font(None, int(settings.resolution_sqrt() / 13))
        title = font.render("Settings", True, colors.black)
        text_rect = title.get_rect(center=(settings.resolution[0] / 2, settings.resolution[1] / 6))
        screen.blit(title, text_rect)

    def draw_resolution_text(self):
        # resolution index
        font = pygame.font.Font(None, int(self.settings.resolution_sqrt() / 24))
        res = str(self.settings_new.resolution[0]) + " x " + str(self.settings_new.resolution[1])
        title = font.render(res, True, colors.black)
        text_rect = title.get_rect(center=(self.settings.resolution[0] / 2, self.settings.resolution[1] / 3.4))
        self.screen.blit(title, text_rect)

        # text
        title = font.render("Resolution:", True, colors.black)
        text_rect = title.get_rect(
            center=(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 3, self.settings.resolution[1] / 3.4))
        self.screen.blit(title, text_rect)

    def create_res(self):

        left = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 9)
        top = int(self.settings.resolution[1] / 3.8 * 1)
        width = int(self.settings.resolution[1] / 20)
        height = width

        btn = Button.button(left, top, width, height, ">", self.settings, 0, self.change_res, "higher")
        self.btn_list.append(btn)

        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 9 - width)
        top = int(self.settings.resolution[1] / 3.8 * 1)

        btn2 = Button.button(left, top, width, height, "<", self.settings, 1, self.change_res, "lower")
        self.btn_list.append(btn2)

    def draw_fullscreen_text(self):
        if self.settings_new.fullscreen:
            res = "Fullscreen"
        else:
            res = "Windowed"

        # ------------ text

        font = pygame.font.Font(None, int(self.settings.resolution_sqrt() / 24))
        title = font.render(res, True, colors.black)
        text_rect = title.get_rect(center=(self.settings.resolution[0] / 2, self.settings.resolution[1] / 3.4 * 1.2))
        self.screen.blit(title, text_rect)
        # ------------- text

        title = font.render("Window Mode:", True, colors.black)
        text_rect = title.get_rect(
            center=(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 3, self.settings.resolution[1] / 3.4 * 1.2))
        self.screen.blit(title, text_rect)

    def create_fullscreen(self):

        left = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 9)
        top = int(self.settings.resolution[1] / 3.8 * 1.22)
        width = int(self.settings.resolution[1] / 20)
        height = width

        btn = Button.button(left, top, width, height, ">", self.settings, 2, self.change_fullscreen)
        self.btn_list.append(btn)

        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 9 - width)
        top = int(self.settings.resolution[1] / 3.8 * 1.22)

        btn2 = Button.button(left, top, width, height, "<", self.settings, 3, self.change_fullscreen)
        self.btn_list.append(btn2)

    def create_exit(self):
        left = int(self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10)
        top = int(
            self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.9 + self.settings.resolution[1] / 11 * 4.8)
        width = int(self.settings.resolution[0] / 2 + self.settings.resolution[0] / 10 - (
                self.settings.resolution[0] / 2 - self.settings.resolution[0] / 10))
        height = int((self.settings.resolution[1] / 2 + self.settings.resolution[1] / 3.7) - (
                self.settings.resolution[1] / 2 - self.settings.resolution[1] / 3.7) / 0.33)

        btn = Button.button(left, top, width, height, "EXIT / Apply", self.settings, 4,
                            self.return_settings)
        self.btn_list.append(btn)

    def draw_all(self):
        pygame.font.init()
        self.screen.fill(colors.white)

        # ---------------
        self.draw_title(self.screen, self.settings)
        self.draw_resolution_text()
        self.draw_fullscreen_text()

        # --------------
        self.draw_buttons()

        return self.settings.resolution != self.settings_new.resolution

    def return_settings(self):
        Saved_Settings.saveSettings(self.settings_new, Saved_Settings.FILENAME)
        print(self.settings_new)
        menu.show_menu(self.settings_new)


def create_revert_button(menu_object):
    for btn in menu_object.btn_list:
        if btn.ID == 6:
            print(len(menu_object.draw_btn_list))
            menu_object.draw_btn_list.append(btn)
            print(len(menu_object.draw_btn_list))
            menu_object.btn_list = []


def initiate(screen, settings, menu_object):
    create_revert_button(menu_object)
    clock = pygame.time.Clock()
    settings_new = Saved_Settings.Settings()
    settings_new.fullscreen = settings.fullscreen
    settings_new.resolution = settings.resolution

    draw_settings = ChangeSettings(screen, settings, settings_new)

    while True:
        clock.tick(60)
        draw_settings.draw_all()

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            #print(event)
        draw_settings.process_event(events)

        pygame.display.flip()

    return settings_new
