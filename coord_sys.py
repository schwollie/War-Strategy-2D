from pygame import Rect


class CoordSys:
    '''Represents a coordinate system, which is defined by a pygame.Rect.

    All points and rectangles are relative to a coordinate system, and coordinate
    systems can be used to transform geometry from one coordinate system into
    another one.
    '''

    def __init__(self, rect):
        self.rect = rect

    def transform_point(self, point, target_sys):
        # Sample:
        #  this.rect(100, 100, 1000, 500)
        #  point(200,450)
        #  target_sys(0, 50, 100, 100)
        #  => result(0+100*(200-100)/1000, 50+100*(450-100)/500) = (10,120)
        x, y = point
        rel_x = (x - self.rect.left) / self.rect.width
        rel_y = (y - self.rect.top) / self.rect.height
        new_x = target_sys.rect.left + target_sys.rect.width * rel_x
        new_y = target_sys.rect.top + target_sys.rect.height * rel_y
        return new_x, new_y

    def transform_rect(self, rect, target_sys):
        new_top_left = self.transform_point(rect.topleft, target_sys)
        new_bottom_right = self.transform_point(rect.bottomright, target_sys)
        return Rect(new_top_left, new_bottom_right)


class CoordPoint:
    def __init__(self, point, coord_sys):
        self.point = point
        self.source_sys = coord_sys

    def transform(self, target_sys):
        self.source_sys.transform_point(self.point, target_sys)


def testCoordSys():
    cs1 = CoordSys(Rect((100, 100), (1000, 500)))
    cs2 = CoordSys(Rect((0, 50), (100, 100)))
    p1_in_cs2 = cs1.transform_point((200, 450), cs2)
    print(p1_in_cs2)
    p1_in_cs1 = cs2.transform_point(p1_in_cs2, cs1)
    print(p1_in_cs1)

testCoordSys()