import pygame

Grass_image = pygame.image.load("images/Grass.jpg")
Dirt_image = pygame.image.load("images/Dirt.jpg")
Water_image = pygame.image.load("images/Water.jpg")
Rock_image = pygame.image.load("images/Rock.jpg")


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Grass_image
        self.rect = self.image.get_rect()
        self.pos_x = pos_x  # in coordinate system 10000 x 10000
        self.pos_y = pos_y  # in coordinate system 10000 x 10000
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.view_pos_x = 0
        self.view_pos_y = 0

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect()


class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Dirt_image
        self.rect = self.image.get_rect()
        self.pos_x = pos_x  # in coordinate system 10000 x 10000
        self.pos_y = pos_y  # in coordinate system 10000 x 10000
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.view_pos_x = 0
        self.view_pos_y = 0

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect()


class Water(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Water_image
        self.rect = self.image.get_rect()
        self.pos_x = pos_x  # in coordinate system 10000 x 10000
        self.pos_y = pos_y  # in coordinate system 10000 x 10000
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.view_pos_x = 0
        self.view_pos_y = 0

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect()


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Rock_image
        self.rect = self.image.get_rect()
        self.pos_x = pos_x  # in coordinate system 10000 x 10000
        self.pos_y = pos_y  # in coordinate system 10000 x 10000
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.view_pos_x = 0
        self.view_pos_y = 0

    def draw(self, screen, pos):
        screen.blit(self.image, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, (int(width), int(height)))
        self.rect = self.image.get_rect()


#
