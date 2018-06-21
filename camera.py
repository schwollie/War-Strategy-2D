import pygame
import math
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
        step = min(dt * self.step_size(), int(vp.top))
        self.move((0, -step))

    def move_down(self, dt):
        vp = self.view_port()
        step = min(dt * self.step_size(), Camera.MAX_Y - vp.bottom)
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
        w, h = pygame.display.get_surface().get_size()
        width = 5000 / self.zoom_level
        height = width*(h/w)
        view_port = Rect(0, 0, 0, 0)
        view_port.size = (width+1, height+1) # +1 to prevent white bars at the bottom or right
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
