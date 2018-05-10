import pygame
import sys
import MapGenerator as mg
import colors
import Sidebar
import Camera


def draw_Blocks(screen):
    Block_List = mg.Map_Tiles_List


    for row in range(mg.block_number_x):
        for col in range(mg.block_number_y):
            if Camera.Camera_pos[0] + Camera.Camera_pos[2] + 200 >= Block_List[row][col].pos_x >= Camera.Camera_pos[0] - 200 and \
               Camera.Camera_pos[1] + 200 >= Block_List[row][col].pos_y >= Camera.Camera_pos[1] - Camera.Camera_pos[3]:

                Block_List[row][col].draw(screen, [Block_List[row][col].view_pos_x, Block_List[row][col].view_pos_y, Block_List[row][col].rect[2], Block_List[row][col].rect[3]])

def draw_fps(screen, dt):
    pygame.font.init()
    font = pygame.font.Font(None, 100)
    fps = str(int(1000/dt))
    title = font.render(fps, True, colors.black)
    text_rect = title.get_rect(center=(100, 100))
    screen.blit(title, text_rect)

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
        #print(clock.get_time())
        delta_time = clock.get_time()


        # -------------------------

        events = pygame.event.get()

        # -----------------------------

        Camera.change_cam(delta_time, events)

        draw_Blocks(screen)
        draw_fps(screen, delta_time)

        bar.draw_all(screen, events)

        for event in events:
            if event == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
