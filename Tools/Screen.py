import curses
from Utils.Vector import Vector
from Utils.Plane import Plane
import math
from bresenham import bresenham

"""
Represents a Console Screen only.
"""


class Screen:
    def __init__(self, width, height, begin_x, begin_y, pixel_correction_scale):
        # where we start drawing from
        origin = Vector(begin_x + width / 2,-(begin_y + height / 2))
        self.display_plane = Plane(origin, Vector(width, height))
        self.window = curses.newwin(height, width, begin_y, begin_x)
        # scale is 1,1 by default
        # however if the travel of one pixel in the vertical or horizontal is
        # unequal such as on the terminal, this can be adjusted here
        # For the terminal the vertical is .467 of the horizontal. to be equal
        self._scale = pixel_correction_scale
        self.should_refresh = True

        self.write_str(Vector(0, 5), 'hello')

        self.refresh()

    def will_write(self):
        if not self.should_refresh:
            self.should_refresh = True
            self.clear()

    def write_str(self, pos, string):
        """
        Draw the position on screen
        :param pos:
        :param string:
        :return:
        """
        self.will_write()
        # pos is the position from the origin
        # so to adjust it we need to subtract half the
        # pos=pos.copy().subtract(self.display_plane.origin)
        try:
            self.window.addstr(-int(pos.y), int(pos.x), string)
        except:
            pass

    def clear(self):
        self.window.erase()

    def refresh(self):
        if self.should_refresh:
            self.window.refresh()
            self.should_refresh = False

    def scale_to_screen(self, vectors):
        for v in vectors:
            # print(self._scale)
            # print(v)
            v.multiply_vector(self._scale)

    def draw_line(self, p_from, p_to):
        """
        y = mx +c
        x = (y-c)/m
        c= y-mx
        :param p_from:
        :param p_to:
        :return:
        """
        # print(p_from,p_to)

        coord_list = list(bresenham(round(p_from.x), round(p_from.y), round(p_to.x), round(p_to.y)))
        # print(coord_list)
        import time
        # time.sleep(15)
        for p in coord_list:
            self.write_str(Vector(p[0], p[1]), '.')

    def draw_shape(self, points):
        num_points = len(points)
        if num_points < 2:
            return
        for i in range(1, num_points):
            self.draw_line(points[i - 1], points[i])
