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
        for col in range(mg.block_number_y):
            if Camera.Camera_pos[0] + Camera.Camera_pos[2] + 200 >= Block_List[row][col].pos_x >= Camera.Camera_pos[0] - 200 and \
               Camera.Camera_pos[1] + 200 >= Block_List[row][col].pos_y >= Camera.Camera_pos[1] - Camera.Camera_pos[3]:

                Block_List[row][col].draw(screen, [Block_List[row][col].view_pos_x, Block_List[row][col].view_pos_y, Block_List[row][col].rect[2], Block_List[row][col].rect[3]])


def initialize_Map(screen, settings):
    clock = pygame.time.Clock()
    mg.init()
    Camera.initialize_cam()

    Camera.transform_blocks()
    Camera.set_Blocks_settings()

    bar = Sidebar.Sidebar(settings)

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

        bar.draw_all(screen, events)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
