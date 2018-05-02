import pygame
import sys
import MapGenerator as mg
import colors
import Settings

Camera_pos = [0, 0, 10000, 10000]  # left, top, width, height
# Camera pos = coordinate system (10000 x 10000) the logic is on that coordinate system too


def draw_Blocks(screen):
    Block_List = mg.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()

    for row in range(mg.block_number_x):
        for col in range(len(Block_List[0])):
            block = Block_List[row][col]
            if block.view_pos_x in range(w) and \
                    block.view_pos_y in range(h):
                block.draw(screen, [block.view_pos_x, block.view_pos_y, block.rect[2], block.rect[3]])
                #print(block.view_pos_x, block.view_pos_y)


def set_Blocks_settings():
    block_list = mg.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()

    for row in range(mg.block_number_x):
        for col in range(mg.block_number_y):
            block = block_list[row][col]
            view_x_pos_first = block.pos_x - Camera_pos[0]  # pos on the screen x
            maßstab_cam_x = Camera_pos[2] / w
            block.view_pos_x = view_x_pos_first/maßstab_cam_x

            view_y_pos_first = block.pos_y - Camera_pos[1]  # pos on the screen y
            maßstab_cam_y = Camera_pos[3] / h
            block.view_pos_y = view_y_pos_first / maßstab_cam_y

            print(block.view_pos_x, block.view_pos_y)


def transform_blocks():
    Block_List = mg.Map_Tiles_List
    w, h = pygame.display.get_surface().get_size()
    for row in range(mg.block_number_x):
        for col in range(mg.block_number_y):
            block = Block_List[row][col]
            print(w/(1/(10000/Camera_pos[2])*mg.block_number_x), (h/(1/(10000/Camera_pos[3])*mg.block_number_y)))
            block.transform_pic(w/(1/(10000/Camera_pos[2])*mg.block_number_x),
                                (h/(1/(10000/Camera_pos[3])*mg.block_number_y)))


def change_cam(delta_time):
    changed = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        Camera_pos[0] = Camera_pos[0] + 0.1 * delta_time
        changed = True
    if keys[pygame.K_a]:
        Camera_pos[0] = Camera_pos[0] - 1 * delta_time
        changed = True
    if keys[pygame.K_s]:
        Camera_pos[1] = Camera_pos[1] + 1 * delta_time
        changed = True
    if keys[pygame.K_w]:
        Camera_pos[1] = Camera_pos[2] - 1 * delta_time
        changed = True

    if changed:
        transform_blocks()
        set_Blocks_settings()


def initialize_Map(screen):
    clock = pygame.time.Clock()
    mg.init()

    transform_blocks()
    set_Blocks_settings()

    while True:
        clock.tick(60)
        delta_time = clock.get_time()
        events = pygame.event.get()
        change_cam(delta_time)

        print(Camera_pos)

        screen.fill(colors.black)

        draw_Blocks(screen)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()