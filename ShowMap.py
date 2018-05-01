import pygame
import sys
import MapGenerator
import colors
import Blocks
import Saved_Settings


def draw_Blocks(screen):
    Block_List = MapGenerator.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()
    #print(screen)

    for row in range(len(Block_List)):
        for col in range(len(Block_List[0])):
            block = Block_List[row][col]
            block.transform_pic(h/MapGenerator.width, h/MapGenerator.height)
            pos_x = h/MapGenerator.width * col
            pos_y = h/MapGenerator.height * row
            block.draw(screen, [pos_x, pos_y, block.rect[2], block.rect[3]])


def initialize_Map(screen):
    clock = pygame.time.Clock()
    MapGenerator.init()

    while True:
        clock.tick(60)
        screen.fill(colors.black)

        draw_Blocks(screen)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()