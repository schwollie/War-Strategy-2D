import math
import pygame
import sys
import MapGenerator as mg
import colors
import Blocks
import Sidebar
import Camera


def draw_Blocks(screen):
    Block_List = mg.Map_Tiles_List

    for row in range(mg.block_number_x):
        for col in range(len(Block_List[0])):
            block = Block_List[row][col]
            # print(int(Camera_pos[1] - Camera_pos[3]), Camera_pos[1], block.pos_y)

            if Camera.Camera_pos[0] + Camera.Camera_pos[2] + 100 >= block.pos_x >= Camera.Camera_pos[0] - 100: #and \
              # Camera.Camera_pos[1] >= block.pos_y <= Camera.Camera_pos[1] - Camera.Camera_pos[3]:
                block.draw(screen, [block.view_pos_x, block.view_pos_y, block.rect[2], block.rect[3]])


def initialize_Map(screen):
    clock = pygame.time.Clock()
    mg.init()
    Camera.initialize_cam()

    Camera.transform_blocks()
    Camera.set_Blocks_settings()

    bar = Sidebar.Sidebar()

    while True:
        screen.fill(colors.white)
        clock.tick(60)
        print(clock.get_time())
        delta_time = clock.get_time()

        # -------------------------

        events = pygame.event.get()

        # -----------------------------

        Camera.change_cam(delta_time, events)

        draw_Blocks(screen)

        bar.draw_rect(screen)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
