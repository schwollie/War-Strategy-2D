import pygame
import sys
import MapGenerator
import Blocks
import Saved_Settings


def draw_Blocks(screen):
    Block_List = MapGenerator.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()


def initialize_Map(screen):
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        draw_Blocks(screen)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()