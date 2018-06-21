import Button
import ImageButton
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

class Items:
    def __init__(self, price, name, left, top, width, height, icon_location, info="100$"):
        self.price = price
        self.name = name
        self.info = info

        self.image_button = ImageButton.ImageButton(icon_location, left, top, width, height)

    def update_price(self, newprice=None, pricemultiplier=None):
        if newprice:
            self.price = newprice
        elif pricemultiplier:
            self.price = self.price*pricemultiplier

    def show_item(self, surface):
        pass

