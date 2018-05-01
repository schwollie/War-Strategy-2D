import pygame


class Grass(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Grass.png")
        self.rect = self.image.get_rect()
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.rect.left = pos_x
        self.rect.top = pos_y

    def draw(self, screen, pos):
        screen.Blit(screen, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, int(width), int(height))
        self.rect = self.image.get_rect()


class Dirt(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Dirt.png")
        self.rect = self.image.get_rect()
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.rect.left = pos_x
        self.rect.top = pos_y

    def draw(self, screen, pos):
        screen.Blit(screen, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, int(width), int(height))
        self.rect = self.image.get_rect()


class Water(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Water.png")
        self.rect = self.image.get_rect()
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.rect.left = pos_x
        self.rect.top = pos_y

    def draw(self, screen, pos):
        screen.Blit(screen, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, int(width), int(height))
        self.rect = self.image.get_rect()


class Rock(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/Rock.png")
        self.rect = self.image.get_rect()
        self.x_pos = pos_x
        self.y_pos = pos_y
        self.rect.left = pos_x
        self.rect.top = pos_y

    def draw(self, screen, pos):
        screen.Blit(screen, pos)

    def transform_pic(self, width, height):
        self.image = pygame.transform.scale(self.image, int(width), int(height))
        self.rect = self.image.get_rect()


#
