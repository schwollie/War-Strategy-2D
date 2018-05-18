import pygame
import sys
import MapGenerator as mg
import colors
import Sidebar
import Camera as cam
import Camera


def draw_Blocks(screen):
    useBetterVersion = True
    if useBetterVersion:
        left, top, w, h = Camera.cam_to_view(Camera.Camera_pos)
        #print("Camera: %s, View: %s" % ((Camera.Camera_pos, (left, top, w, h))))
        screen.blit(cam.map_active_draw, (0, 0), (left, top, w, h))
    else:
        Block_List = mg.Map_Tiles_List
        for row in range(mg.block_number_x):
            for col in range(mg.block_number_y):
                    Block_List[row][col].draw(screen)


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
        delta_time = clock.get_time()

        # -------------------------

        events = pygame.event.get()

        # -----------------------------

        Camera.change_cam(delta_time, events)

        draw_Blocks(screen)

        bar.draw_all(screen, events, delta_time)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
