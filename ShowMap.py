import math

import pygame
import sys
import MapGenerator as mg
import colors
import Blocks
import Sidebar


Camera_pos = [0, 0, 0, 0]  # left, top, width, height
# Camera pos = coordinate system (10000 x 10000) the logic is on that coordinate system too


def draw_Blocks(screen):
    Block_List = mg.Map_Tiles_List
#    w, h = pygame.display.get_surface().get_size()

    for row in range(mg.block_number_x):
        for col in range(len(Block_List[0])):
            block = Block_List[row][col]
            #print(int(Camera_pos[1] - Camera_pos[3]), Camera_pos[1], block.pos_y)

            #if int(block.pos_x) in range(int(Camera_pos[0]-1000), int(Camera_pos[0]) + Camera_pos[2] + 1000) and \
                   #int(block.pos_y) in range(int(Camera_pos[1] - Camera_pos[3]-1000), int(Camera_pos[1]+1000)):
            block.draw(screen, [block.view_pos_x, block.view_pos_y, block.rect[2], block.rect[3]])


def set_Blocks_settings():
    block_list = mg.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()

    maßstab_cam_x = Camera_pos[2] / w
    maßstab_cam_y = Camera_pos[3] / h

    for row in range(mg.block_number_y):
        for col in range(mg.block_number_x):
            block = block_list[row][col]

            view_x_pos_first = block.pos_x - Camera_pos[0]  # pos on the screen x
            block.view_pos_x = int(view_x_pos_first/maßstab_cam_x)

            view_y_pos_first = Camera_pos[1] - block.pos_y    # pos on the screen y
            block.view_pos_y = int(view_y_pos_first / maßstab_cam_y)

            # print(block.view_pos_x, block.view_pos_y, "Block_settings")


def transform_blocks():
    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_width = math.ceil(w / (dx * mg.block_number_x))
    new_height = math.ceil(h / (dy * mg.block_number_y))

    Blocks.resize_pics(new_width, new_height)

    block_list = mg.Map_Tiles_List
    for row in range(mg.block_number_y):
        for col in range(mg.block_number_x):
            block_list[row][col].update_rect()

def change_cam(delta_time, events):
    changed = False

    keys = pygame.key.get_pressed()

    w, h = pygame.display.get_surface().get_size()

    zoom_level = Camera_pos[2]/10000

    if keys[pygame.K_d]:
        Camera_pos[0] = int(Camera_pos[0] + 10 * delta_time * zoom_level)
        changed = True
    if keys[pygame.K_a]:
        Camera_pos[0] = int(Camera_pos[0] - 10 * delta_time * zoom_level)
        changed = True
    if keys[pygame.K_s]:
        Camera_pos[1] = int(Camera_pos[1] - 10 * delta_time * zoom_level)
        changed = True
    if keys[pygame.K_w]:
        Camera_pos[1] = int(Camera_pos[1] + 10 * delta_time * zoom_level)
        changed = True

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                Camera_pos[2] -= 1000 * zoom_level
#                Camera_pos[3] -= 1000 * zoom_level
                Camera_pos[3] = Camera_pos[2] * (h / w)
                changed = True
            if event.button == 5:
                Camera_pos[2] += 1000 * zoom_level
#                Camera_pos[3] += 1000 * zoom_level
                Camera_pos[3] = Camera_pos[2] * (h / w)
                changed = True

    if changed:
        set_Blocks_settings()
        transform_blocks()
        return
    return


def initialize_Map(screen):
    global Camera_pos
    w, h = pygame.display.get_surface().get_size()
    initiales_cam_y = 1000 * (h / w)
    Camera_pos = [0, 10000, 1000, initiales_cam_y]
    clock = pygame.time.Clock()
    mg.init()

    transform_blocks()
    set_Blocks_settings()

    while True:
        clock.tick(60)
        delta_time = clock.get_time()
        events = pygame.event.get()
        change_cam(delta_time, events)

        print(clock.get_time())

        screen.fill(colors.white)

        draw_Blocks(screen)
        #Sidebar.draw_rect(screen)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()