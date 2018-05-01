import pygame
import sys
import MapGenerator
import Blocks
import Saved_Settings


MapGenerator.init()


def draw_Blocks(screen):
    Block_List = MapGenerator.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()

    for row in range(len(Block_List)):
        for col in range(len(Block_List[0])):
            Block = Block_List[row][col]
            Block.transform_pic(Block, w/MapGenerator.width, h/MapGenerator.height)
            pos_x = w/MapGenerator.width * row
            pos_y = h/MapGenerator.height * col
            Block.draw(screen, [pos_x, pos_y, Block.rect[2], Block.rect[3]])


def initialize_Map(screen):
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)


        draw_Blocks(screen)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()