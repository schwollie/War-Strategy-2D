import Button
import pygame

class Shop(object):
    def __init__(self, settings):
        self.shop_btn_list = []
        self.available_items = []     # Items in the sidebar which can be selected an then can be placed
        self.settings = settings
        self.initialize_buttons()

    def initialize_buttons(self):
        w, h = pygame.display.get_surface().get_size()

        # ---- Shop expand button
        left = int(w-(w*0.18))
        top = int(h-(h*0.835))
        width = int(w*0.1)
        height = int(h*0.07)
        shop_btn = Button.button(left, top, width, height, "Shop", self.settings)
        self.shop_btn_list.append(shop_btn)

    def show(self, screen):
        for btn in self.shop_btn_list:
            btn.draw_btn(screen)

    def process_events(self, events):
        for btn in self.shop_btn_list:
            btn.check_click_collide(events)

    def expand_shop(self):
        pass


