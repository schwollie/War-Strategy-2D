import pygame
import colors
import Button
import ImageButton
import PlayerStats
import sys

Swordsman_image_file = 'images/Swordsman.png'
Bowman_image_file = 'images/Bowman.png'


class Sidebar(pygame.sprite.Sprite):
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)
        self.show_sidebar = True
        self.settings = settings
        self.btn_list = []
        self.img_btn_list = []
        self.button_list = []
        self.create_toggle_button()
        self.create_swordsman_image()
        self.create_bowman_image()
        self.create_exit_button()

    def change_sidebar_visibility(self):
        if self.show_sidebar:
            self.show_sidebar = False
        else:
            self.show_sidebar = True

    def draw_fps(self, screen, dt):
        w, h = pygame.display.get_surface().get_size()
        pygame.font.init()
        font = pygame.font.Font(None, int(w/25))
        fps = str(int(1000 / dt))
        title = font.render(("FPS: " + fps), True, colors.black)
        text_rect = title.get_rect(topleft=(w-(w*0.18), h-(h*0.965)))
        screen.blit(title, text_rect)

    def create_swordsman_image(self):
        w, h = pygame.display.get_surface().get_size()
        width = int(w*0.07)
        height = width
        left = w-(w*0.18)
        top = h-(h*0.7)

        img_btn = ImageButton.ImageButton(Swordsman_image_file, left, top, width, height, self.settings, 1)
        self.btn_list.append(img_btn)

    def create_bowman_image(self):
        w, h = pygame.display.get_surface().get_size()
        width = int(w * 0.07)
        height = width
        left = w-(w*0.095)
        top = h-(h*0.7)

        img_btn = ImageButton.ImageButton(Bowman_image_file, left, top, width, height, self.settings, 1)
        self.btn_list.append(img_btn)

    def create_shop_button(self):
        w, h = pygame.display.get_surface().get_size()
        left = int(w-(w*0.18))
        top = int(h-(h*0.20))
        width = w*0.17
        height = h*0.17
        self.btn_shop = Button.button(left, top, width, height, "SHOP!")


    def create_exit_button(self):
        w, h = pygame.display.get_surface().get_size()
        left = int(w-(w*0.18))
        top = int(h-(h*0.10))
        width = int(w*0.17)
        height = int(h*0.07)

        btn = Button.button(left, top, width, height, "EXIT", self.settings, function_to_call=sys.exit)
        self.btn_list.append(btn)

    def draw_rect(self, screen):
        w, h = pygame.display.get_surface().get_size()
        pygame.draw.rect(screen, colors.red, (w-(0.2*w), 0, w-(0.2*w), h))
        pygame.draw.rect(screen, colors.dark_grey, (w - (0.2 * w), -100, w - (0.2 * w), (h+200)), int(w/50))

    def draw_gold(self, screen):
        Gold = PlayerStats.Gold
        w, h = pygame.display.get_surface().get_size()
        pygame.font.init()
        font = pygame.font.Font(None, int(w / 25))
        title = font.render(("Gold: " + str(Gold)), True, colors.black)
        text_rect = title.get_rect(topleft=(w - (w * 0.18), h - (h * 0.9)))
        screen.blit(title, text_rect)

    def create_toggle_button(self):
        # big rect
        w, h = pygame.display.get_surface().get_size()
        left = w-(w*0.08)
        top = h-(h*0.98)
        width = w*0.05
        height = h*0.05
        self.toggle_btn = Button.button(left, top, width, height, "+/-", self.settings, 1, function_to_call=self.change_sidebar_visibility)
        self.btn_list.append(self.toggle_btn)

    def draw_all(self, screen, dt):
        if self.show_sidebar:
            self.draw_rect(screen)
            self.draw_gold(screen)
            self.draw_fps(screen, dt)
            for btn in self.btn_list:
                btn.draw_btn(screen)
        else:
            self.toggle_btn.draw_btn(screen)

    def process_event(self, event):
        if self.show_sidebar:
            for btn in self.btn_list:
                if btn.check_click_collide(event):
                    btn.action()
        else:
            if self.toggle_btn.check_click_collide(event):
                self.toggle_btn.action()







