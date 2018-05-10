import pygame
import math
import MapGenerator as mg
import Blocks

Camera_pos = [0, 0, 0, 0]  # left, top, width, height
# Camera pos = coordinate system (10000 x 10000) the logic is on that coordinate system too


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
    changed_pos = False
    changed_size = False

    keys = pygame.key.get_pressed()

    w, h = pygame.display.get_surface().get_size()

    zoom_level = Camera_pos[2]/10000

    if keys[pygame.K_d] and Camera_pos[0] + Camera_pos[2] < 10000:
        Camera_pos[0] = int(Camera_pos[0] + 6 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_a] and Camera_pos[0] > 1:
        Camera_pos[0] = int(Camera_pos[0] - 6 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_s] and Camera_pos[1] - Camera_pos[3] > 0:
        Camera_pos[1] = int(Camera_pos[1] - 6 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_w] and Camera_pos[1] < 10000:
        Camera_pos[1] = int(Camera_pos[1] + 6 * delta_time * zoom_level)
        changed_pos = True

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            zoom_level = zoom_level**1.4
            if event.button == 4 and Camera_pos[2] > 500:
                Camera_pos[2] -= 2000 * zoom_level / 2
                Camera_pos[3] = Camera_pos[2] * (h / w)
                Camera_pos[0] += 2000 * zoom_level / 4
                Camera_pos[1] -= 2000*zoom_level / 4 * (h/w)
                changed_size = True
            if event.button == 5 and Camera_pos[2] < 9000:
                Camera_pos[2] += 2000 * zoom_level / 2
                Camera_pos[3] = Camera_pos[2] * (h / w)
                Camera_pos[0] -= 2000 * zoom_level / 4
                Camera_pos[1] += 2000 * zoom_level / 4 * (h / w)
                changed_size = True

    if changed_pos or changed_size:

        if Camera_pos[0] + Camera_pos[2] > 10000:
            Camera_pos[0] = 10000 - Camera_pos[2]

        if Camera_pos[0] < 0:
            Camera_pos[0] = 0

        if Camera_pos[1] - Camera_pos[3] < 0:
            Camera_pos[1] = Camera_pos[3]

        if Camera_pos[1] > 10000:
            Camera_pos[1] = 10000

        set_Blocks_settings()


    if changed_size:
        transform_blocks()
        set_Blocks_settings()

    #print(Camera_pos)

    return


def initialize_cam():
    global Camera_pos
    w, h = pygame.display.get_surface().get_size()
    initiales_cam_y = 5000 * (h / w)
    Camera_pos = [0, 10000, 5000, initiales_cam_y]