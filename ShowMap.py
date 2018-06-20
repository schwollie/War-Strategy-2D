import pygame
import sys
import MapGenerator as mg
import colors
import Sidebar
import camera as cam
from blocks import BlockMap
from camera import Camera


def draw_Blocks(screen):
    left, top, w, h = Camera.cam_to_view(Camera.Camera_pos)
    #print("Camera: %s, View: %s" % ((Camera.Camera_pos, (left, top, w, h))))
    screen.blit(cam.map_active_draw, (0, 0), (left, top, w, h))


def initialize_Map(screen, settings):
    clock = pygame.time.Clock()
    map = mg.init(200, 200, screen, settings)

    w, h = pygame.display.get_surface().get_size()
    camera = Camera(w/h)
    #Camera.initialize_cam()
    #Camera.transform_blocks()
    #Camera.set_Blocks_settings()

    block_map = BlockMap(map)
    vw, vh = w * 2 * camera.zoom_level, h * 2 * camera.zoom_level
    block_map.update(vw, vh)

    vp_in_block = calc_view_port(camera, block_map)

    bar = Sidebar.Sidebar(settings)
    move_up = False
    move_down = False
    move_left = False
    move_right = False
    zoom_in = False
    zoom_out = False

    while True:
        screen.fill(colors.white)
        clock.tick(120)

        delta_time = clock.get_time()
        #print(delta_time)

        # -------------------------

        events = pygame.event.get()

        # -----------------------------

        #Camera.change_cam(delta_time, events)

        changed_pos = False
        changed_size = False

        for event in events:
            if event == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    camera.zoom_in()
                    changed_size = True
                if event.button == 5:
                    camera.zoom_out()
                    changed_size = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_PLUS:
                    zoom_in = True
                if event.key == pygame.K_MINUS:
                    zoom_out = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    move_down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_PLUS:
                    zoom_in = False
                if event.key == pygame.K_MINUS:
                    zoom_out = False

        bar.process_event(events)

        if move_up:
            camera.move_up(delta_time)
            changed_pos = True
        if move_left:
            camera.move_left(delta_time)
            changed_pos = True
        if move_down:
            camera.move_down(delta_time)
            changed_pos = True
        if move_right:
            camera.move_right(delta_time)
            changed_pos = True
        if zoom_in:
            camera.zoom_in()
            changed_size = True
        if zoom_out:
            camera.zoom_out()
            changed_size = True

        if changed_size:
            # transform_blocks()
            # set_Blocks_settings()
            vw, vh = w * 2 * camera.zoom_level, h * 2 * camera.zoom_level
            block_map.update(vw, vh)

        if changed_pos or changed_size:
            vp_in_block = calc_view_port(camera, block_map)
            print(camera.view_port(), vp_in_block)

        block_map.draw(screen, vp_in_block)
        bar.draw_all(screen, delta_time)

        pygame.display.flip()


def calc_view_port(camera, block_map):
    vp_in_cam = camera.view_port()
    return camera.coord_sys.transform_rect(vp_in_cam, block_map.coord_sys)
