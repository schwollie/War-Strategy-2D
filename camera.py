import pygame
import math
import MapGenerator as mg
import blocks
from coord_sys import CoordSys
from pygame import Rect

Camera_pos = [0, 0, 0, 0]  # left, top, width, height
# Camera pos = coordinate system (10000 x 10000) the logic is on that coordinate system too

map_high_standard = None
map_mid_standard = None
map_low_standard = None

map_active_draw = None

map_view_pos = [0, 0]


class Camera:
    MIN_X = 0
    MAX_X = 10000
    MIN_Y = 0
    MAX_Y = 10000
    MIN_ZOOM = 0.5
    MAX_ZOOM = 1.3
    STEP_SIZE_ON_LEVEL_1 = 5

    def __init__(self, aspect_ratio):
        self.ratio = aspect_ratio
        self.pos = (5000, 5000)
        self.coord_sys = CoordSys(Rect((0, 0), (10000, 10000)))
        self.zoom_level = Camera.MIN_ZOOM

    def move_up(self, dt):
        vp = self.view_port()
        step = min(dt * self.step_size(), vp.top)
        self.move((0, -step))

    def move_down(self, dt):
        vp = self.view_port()
        step = min(dt * self.step_size(), Camera.MAX_Y - vp.bottom)
        print(self.view_port())
        self.move((0, step))

    def move_left(self, dt):
        vp = self.view_port()
        step = min(dt * self.step_size(), vp.left)
        self.move((-step, 0))

    def move_right(self, dt):
        vp = self.view_port()
        step = min(dt * self.step_size(), Camera.MAX_X - vp.right)
        self.move((step, 0))

    def move(self, offset):
        x, y = self.pos
        dx, dy = offset
        self.pos = (x + dx, y + dy)

    def step_size(self):
        return Camera.STEP_SIZE_ON_LEVEL_1 / self.zoom_level

    def zoom_in(self):
        self.zoom_level = min(self.zoom_level + 0.25, Camera.MAX_ZOOM)
        self.clamp()

    def zoom_out(self):
        self.zoom_level = max(self.zoom_level - 0.25, Camera.MIN_ZOOM)
        self.clamp()

    def clamp(self):
        vp = self.view_port()
        x, y = self.pos
        if vp.left < 0:
            x -= vp.left
        if vp.top < 0:
            y -= vp.top
        if vp.right > Camera.MAX_X:
            x -= vp.right - Camera.MAX_X
        if vp.bottom > Camera.MAX_Y:
            y -= vp.bottom - Camera.MAX_Y
        self.pos = (x, y)

    def view_port(self):
        width = 5000 / self.zoom_level
        view_port = Rect(0, 0, 0, 0)
        view_port.size = (width, width)
        view_port.center = self.pos
        return view_port


def testCamera():
    dt = 60
    cam = Camera(480/640)
    print(cam.view_port())
    cam.zoom_in()
    print(cam.view_port())
    cam.zoom_in()
    print(cam.view_port())
    cam.move_up(dt)
    print("up", cam.view_port())
    cam.move_down(dt)
    print("down", cam.view_port())
    cam.move_left(dt)
    print("left", cam.view_port())
    cam.move_right(dt)
    print("right", cam.view_port())
    cam.zoom_out()
    print(cam.view_port())

#testCamera()

'''
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


def set_map_settings():
    w, h = pygame.display.get_surface().get_size()
    global map_view_pos

    maßstab_cam_x = Camera_pos[2] / w
    maßstab_cam_y = Camera_pos[3] / h

    view_x_pos_first = 0 - Camera_pos[0]  # pos on the screen x
    map_view_pos[0] = int(view_x_pos_first / maßstab_cam_x)

    view_y_pos_first = Camera_pos[1] - 0  # pos on the screen y
    map_view_pos[1] = int(view_y_pos_first / maßstab_cam_y)


def transform_blocks():
    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_block_width = int(math.ceil(w / (dx * mg.block_number_x)))
    new_block_height = int(math.ceil(h / (dy * mg.block_number_y)))

    Blocks.resize_pics(new_block_width, new_block_height)

    #global map_low
    #map_low = pygame.Surface((new_block_width * mg.block_number_x, new_block_height * mg.block_number_y))

    block_list = mg.Map_Tiles_List
    y = 0
    for row in range(mg.block_number_y):
        x = 0
        for col in range(mg.block_number_x):
            block = block_list[row][col]
            block.update_rect()
            block.view_pos_x = x
            block.view_pos_y = y
            #block.draw(map_low)
            x += new_block_width
        y += new_block_height
    # pygame.image.save(map_low, "images/temp/map.jpg")


def transform_map():
    global map_high_standard
    global map_mid_standard
    global map_low_standard
    global map_active_draw

    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_block_width = int(math.ceil(w / (dx * mg.block_number_x)))
    new_block_height = int(math.ceil(h / (dy * mg.block_number_y)))

    width = int(new_block_width*mg.block_number_x)
    height = int(new_block_height*mg.block_number_y)

    if Camera_pos[2] > 8500:
        map_active_draw = pygame.transform.scale(map_low_standard, (width, height))
    elif Camera_pos[2] > 5500:
        map_active_draw = pygame.transform.scale(map_mid_standard, (width, height))
    else:
        map_active_draw = pygame.transform.scale(map_high_standard, (width, height))


def render_map_pics():
    w, h = pygame.display.get_surface().get_size()
    global map_high_standard
    global map_mid_standard
    global map_low_standard
    global map_active_draw
    global Camera_pos

    # ---------------------------------------------- high

    Camera_pos = [0, 0, 3000, 3000*(h / w)]
    transform_blocks()

    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_block_width = int(math.ceil(w / (dx * mg.block_number_x)))
    new_block_height = int(math.ceil(h / (dy * mg.block_number_y)))

    map_high_standard = pygame.Surface((new_block_width * mg.block_number_x, new_block_height * mg.block_number_y)).convert()

    block_list = mg.Map_Tiles_List
    y = 0
    for row in range(mg.block_number_y):
        x = 0
        for col in range(mg.block_number_x):
            block = block_list[row][col]
            block.update_rect()
            block.view_pos_x = x
            block.view_pos_y = y
            block.draw(map_high_standard)
            x += new_block_width
        y += new_block_height
    #pygame.image.save(map_high, "images/temp/map_high.jpg")

    # ---------------------------------------------- mid

    Camera_pos = [0, 0, 5500, 5500*(h / w)]
    transform_blocks()

    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_block_width = int(math.ceil(w / (dx * mg.block_number_x)))
    new_block_height = int(math.ceil(h / (dy * mg.block_number_y)))

    map_mid_standard = pygame.Surface((new_block_width * mg.block_number_x, new_block_height * mg.block_number_y)).convert()

    block_list = mg.Map_Tiles_List
    y = 0
    for row in range(mg.block_number_y):
        x = 0
        for col in range(mg.block_number_x):
            block = block_list[row][col]
            block.update_rect()
            block.view_pos_x = x
            block.view_pos_y = y
            block.draw(map_mid_standard)
            x += new_block_width
        y += new_block_height
    #pygame.image.save(map_mid, "images/temp/map_mid.jpg")

    # ---------------------------------------------- mid

    Camera_pos = [0, 0, 8500, 8500*(h / w)]
    transform_blocks()

    dx = 1 / (10000 / Camera_pos[2])
    dy = 1 / (10000 / Camera_pos[3])
    w, h = pygame.display.get_surface().get_size()
    new_block_width = int(math.ceil(w / (dx * mg.block_number_x)))
    new_block_height = int(math.ceil(h / (dy * mg.block_number_y)))

    map_low_standard = pygame.Surface((new_block_width * mg.block_number_x, new_block_height * mg.block_number_y)).convert()

    block_list = mg.Map_Tiles_List
    y = 0
    for row in range(mg.block_number_y):
        x = 0
        for col in range(mg.block_number_x):
            block = block_list[row][col]
            block.update_rect()
            block.view_pos_x = x
            block.view_pos_y = y
            block.draw(map_low_standard)
            x += new_block_width
        y += new_block_height
    #pygame.image.save(map_low, "images/temp/map_low.jpg")

    # ------------------------

    Camera_pos = [0, 0, 5000, 5000*(h / w)]
    map_active_draw = map_mid_standard


def change_cam(delta_time, events):
    changed_pos = False
    changed_size = False

    keys = pygame.key.get_pressed()

    w, h = pygame.display.get_surface().get_size()

    zoom_level = Camera_pos[2]/10000

    if keys[pygame.K_d] and Camera_pos[0] + Camera_pos[2] < 10000:
        Camera_pos[0] = int(Camera_pos[0] + 15 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_a] and Camera_pos[0] > 1:
        Camera_pos[0] = int(Camera_pos[0] - 15 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_s] and Camera_pos[1] - Camera_pos[3] > 0:
        Camera_pos[1] = int(Camera_pos[1] - 15 * delta_time * zoom_level)
        changed_pos = True
    if keys[pygame.K_w] and Camera_pos[1] < 10000:
        Camera_pos[1] = int(Camera_pos[1] + 15 * delta_time * zoom_level)
        changed_pos = True

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            zoom_level = zoom_level**1.4
            if event.button == 4 and Camera_pos[2] > 1000:
                Camera_pos[2] -= 2000 * zoom_level / 2
                Camera_pos[3] = Camera_pos[2] * (h / w)
                Camera_pos[0] += 2000 * zoom_level / 4
                Camera_pos[1] -= 2000*zoom_level / 4 * (h/w)
                changed_size = True
            if event.button == 5 and Camera_pos[2] < 10000:
                Camera_pos[2] += 2000 * zoom_level / 2
                Camera_pos[3] = Camera_pos[2] * (h / w)
                Camera_pos[0] -= 2000 * zoom_level / 4
                Camera_pos[1] += 2000 * zoom_level / 4 * (h / w)
                changed_size = True

    if changed_pos or changed_size:
        if Camera_pos[0] + Camera_pos[2] > 10000:
            Camera_pos[0] = 10000 - Camera_pos[2]
            #print("too far")
            #print(Camera_pos)

        if Camera_pos[0] < 0:
            Camera_pos[0] = 0
            #print("too far")
            #print(Camera_pos)

        if Camera_pos[1] - Camera_pos[3] < 0:
            Camera_pos[1] = Camera_pos[3]
            #print("too far")
            #print(Camera_pos)

        if Camera_pos[1] > 10000:
            Camera_pos[1] = 10000
            #print("too far")
            #print(Camera_pos)

        set_Blocks_settings()

    if changed_size:
        #transform_blocks()
        #set_Blocks_settings()
        set_map_settings()
        transform_map()

    return


def initialize_cam():
    global Camera_pos
    w, h = pygame.display.get_surface().get_size()
    initiales_cam_y = 5000 * (h / w)
    Camera_pos = [0, 10000, 5000, initiales_cam_y]
    set_Blocks_settings()
    render_map_pics()
    #transform_blocks()


def view_to_cam(x,y):
    w, h = pygame.display.get_surface().get_size()
    left = 10000 * x/w
    top = 10000 * (1 - y/h)
    return (left,top)


def cam_to_view(cam):
    dx = 1.0 / (10000 / cam[2])
    dy = 1.0 / (10000 / cam[3])
    vp_w, vp_h = pygame.display.get_surface().get_size()
    b_w = int(math.ceil(vp_w / (dx * mg.block_number_x)))
    b_h = int(math.ceil(vp_h / (dy * mg.block_number_y)))
    v_w, v_h = int(b_w*mg.block_number_x), int(b_h * mg.block_number_y)
    #print (vp_w, vp_h, b_w, b_h, v_w,v_h)
    left = int(v_w * (cam[0] / 10000.0))
    top = int(v_h * ((10000 - cam[1]) / 10000.0))
    return (left,top, vp_w, vp_h)
'''