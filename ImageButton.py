import pygame
import math
import colors


class ImageButton(object):
    def __init__(self, image_location,  left, top, width, height, settings, ID, function_to_call=None, arguments=None):
        self.arg = arguments
        self.ID = ID
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.settings = settings
        self.line_strength = int((math.sqrt(self.settings.resolution[0] * self.settings.resolution[1]) / 300))
        self.text_size = int(self.settings.resolution_sqrt() / 24)
        self.function_to_call = function_to_call
        self.clock = pygame.time.Clock()
        self.time_2 = 100
        self.time = 200 # in ms
        self.color = colors.white
        self.selected = False
        self.image_loc = image_location
        self.image = pygame.image.load(image_location).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.Animation = False

        # - make a copy for animation: Those vars  shouldn't be changed
        self.saved_left = self.left
        self.saved_top = self.top
        self.saved_width = self.width
        self.saved_height = self.height

    def sound(self):
        sound = pygame.mixer.Sound("SOUND/Click.WAV")
        sound.set_volume(0.1)
        sound.play()

    def block_click(self):
        self.time = self.time - self.clock.get_time()

        if self.time < 0:
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.mouse.get_pressed())
        else:
            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.mouse.get_pressed())

    def click_animation(self):
        self.time_2 = self.time_2 - self.clock.get_time()

        if self.time_2 > 0:
            self.left = self.saved_left + self.settings.resolution[0]/200
            self.top = self.saved_top + self.settings.resolution[0]/200
            self.width = int(self.saved_width - self.settings.resolution[0]/200*2)
            self.height = int(self.saved_height - self.settings.resolution[0]/200*2)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        elif self.time_2 < 0:
            self.left = self.saved_left
            self.top = self.saved_top
            self.width = self.saved_width
            self.height = self.saved_height
            self.image = pygame.image.load(self.image_loc).convert()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.Animation = False

    def draw_btn(self, screen):

        self.clock.tick()

        # update blocking

        if self.time > -1000:
            self.block_click()

        # --------- animation

        if self.Animation:
            self.click_animation()

        if self.check_collide(pygame.mouse.get_pos()):
            self.color = colors.white
        else:
            self.color = colors.black

        screen.blit(self.image, [self.left, self.top, self.rect[2], self.rect[3]])

        pygame.draw.rect(screen, self.color, [self.left, self.top,
                                              self.width, self.height],
                         self.line_strength)

    def check_collide(self, pos):
        x, y = pos

        return self.left <= x <= self.left + self.width \
               and self.top <= y <= self.top + self.height

    def set_unselected(self):
        self.selected = False

    def set_selected(self):
        self.selected = True

    def check_click_collide(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #self.time = 150
                self.time_2 = 100
                if self.check_collide(pygame.mouse.get_pos()):
                    #self.time = 300
                    self.sound()
                    self.Animation = True
                    self.set_selected()
                    return True
            return False

    def action(self):  # what happens if the button gets pushed
        if self.function_to_call:
            if self.arg:
                self.function_to_call(self.arg)
            else:
                self.function_to_call()
        else:
            pass


class ActiveImageButton(object):
    def __init__(self, image_location,  left, top, width, height, settings, ID, function_to_call=None, arguments=None, active=False):
        self.active = active
        self.arg = arguments
        self.ID = ID
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.settings = settings
        self.line_strength = int((math.sqrt(self.settings.resolution[0] * self.settings.resolution[1]) / 300))
        self.text_size = int(self.settings.resolution_sqrt() / 24)
        self.function_to_call = function_to_call
        self.clock = pygame.time.Clock()
        self.time_2 = 100
        self.time = 200 # in ms
        self.color = colors.white
        self.image_loc = image_location
        self.image = pygame.image.load(image_location).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.Animation = False

        # - make a copy for animation: Those vars  shouldn't be changed
        self.saved_left = self.left
        self.saved_top = self.top
        self.saved_width = self.width
        self.saved_height = self.height

    def sound(self):
        sound = pygame.mixer.Sound("SOUND/Click.WAV")
        sound.set_volume(0.1)
        sound.play()

    def block_click(self):
        self.time = self.time - self.clock.get_time()

        if self.time < 0:
            pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
            pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_allowed(pygame.mouse.get_pressed())
        else:
            pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.mouse.get_pressed())

    def click_animation(self):
        self.time_2 = self.time_2 - self.clock.get_time()

        if self.time_2 > 0:
            self.left = self.saved_left + self.settings.resolution[0]/200
            self.top = self.saved_top + self.settings.resolution[0]/200
            self.width = int(self.saved_width - self.settings.resolution[0]/200*2)
            self.height = int(self.saved_height - self.settings.resolution[0]/200*2)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

        elif self.time_2 < 0:
            self.left = self.saved_left
            self.top = self.saved_top
            self.width = self.saved_width
            self.height = self.saved_height
            self.image = pygame.image.load(self.image_loc).convert()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

            self.Animation = False

    def check_legal_selected(self, btnlist):    # only one button object can be active at a time
        for btn in btnlist:
            try:
                if btn.selected:
                    self.set_unselected()
            except NameError:
                pass

    def draw_btn(self, screen):

        self.clock.tick()

        # update blocking

        if self.time > -1000:
            self.block_click()

        # --------- animation

        if self.Animation:
            self.click_animation()

        if self.check_collide(pygame.mouse.get_pos()) or self.active:
            self.color = colors.white
        else:
            self.color = colors.black

        screen.blit(self.image, [self.left, self.top, self.rect[2], self.rect[3]])

        pygame.draw.rect(screen, self.color, [self.left, self.top,
                                              self.width, self.height],
                         self.line_strength)

    def check_collide(self, pos):
        x, y = pos

        return self.left <= x <= self.left + self.width \
               and self.top <= y <= self.top + self.height

    def set_unselected(self):
        self.active = False

    def set_selected(self):
        self.active = True

    def select(self):
        if self.active:
            self.set_unselected()
        else:
            self.set_selected()

    def check_click_collide(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #self.time = 150
                self.time_2 = 100
                if self.check_collide(pygame.mouse.get_pos()):
                    #self.time = 300
                    self.sound()
                    self.Animation = True
                    self.select()
                    return True
            return False

    def action(self):  # what happens if the button gets pushed
        if self.function_to_call:
            if self.arg:
                self.function_to_call(self.arg)
            else:
                self.function_to_call()
        else:
            pass