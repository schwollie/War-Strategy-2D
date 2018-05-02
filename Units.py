import pygame
import Troups


class UnitSwordsmen(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.rotation = 0
        self.pos = pos
        self.alive_troups = []
        self.dead_troups = []
        self.troups_number = 30
        self.rows = 3  # how many Rows there are

        for i in range(0, self.troups_number/self.rows):
            warrior = Troups.Swordsman(((self.pos[0] + i), (self.pos[1])))
            self.alive_troups.append(warrior)
            print(warrior)
        for i in range(0, self.troups_number/self.rows):
            warrior = Troups.Swordsman(((self.pos[0] + i), (self.pos[1])+1))
            self.alive_troups.append(warrior)
        for i in range(0, self.troups_number/self.rows):
            warrior = Troups.Swordsman(((self.pos[0] + i), (self.pos[1])+2))
            self.alive_troups.append(warrior)



    def rotate(self, rotation):
        self.rotation = rotation


sw = UnitSwordsmen((10, 10))