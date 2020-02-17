from Utils.Vector import Vector
from Utils.Plane import Plane
import time
from Utils.Timer import Timer

"""
Represents a camera, an abstraction 
"""


class Camera:
    def __init__(self, view_origin, view_dim, screen):
        self.view_plane = Plane(view_origin, view_dim)
        self.screen = screen
        self.zoom_in = Timer()
        self.zoom_out = Timer()
        self.move_left = Timer()
        self.move_right = Timer()
        self.move_up = Timer()
        self.move_down = Timer()
        self.zoom_max = 10
        self.zoom_min = 1
        self.move_sensitivity = 10
        self.zoom_sensitivity = 10

        self.key_events = {
            'r': self.toggle_zoom_in,
            'e': self.toggle_zoom_out,
            'right': self.toggle_move_right,
            'left': self.toggle_move_left,
            'up': self.toggle_move_up,
            'down': self.toggle_move_down
        }

    def update(self):
        self.move()
        self.zoom()

    def move(self):
        y_move = self.move_up.lap() - self.move_down.lap()
        x_move = self.move_right.lap() - self.move_left.lap()
        self.view_plane.origin.add(Vector(x_move * self.move_sensitivity, y_move * self.move_sensitivity))

    def zoom(self):
        to_zoom = self.zoom_in.lap() - self.zoom_out.lap()
        to_zoom *= self.zoom_sensitivity
        self.view_plane.dim.add(Vector(to_zoom, to_zoom))

        self.screen.write_str(Vector(0, 0), self.view_plane.dim.__str__())

    def key_down(self, key):
        # self.screen.write_str(Vector(1, 1), 'down: ' + key)
        if key in self.key_events:
            self.key_events[key](True)

    def key_up(self, key):
        # self.screen.write_str(Vector(1, 1), 'up: ' + key)

        if key in self.key_events:
            self.key_events[key](False)

    def toggle_zoom_in(self, key_down):
        if key_down:
            if not self.zoom_in.running:
                self.zoom_in.start()
        else:
            self.screen.write_str(Vector(0, 7), self.zoom_in.poll().__str__())
            self.zoom_in.stop()

    def toggle_zoom_out(self, key_down):
        if key_down:
            if not self.zoom_out.running:
                self.zoom_out.start()
        else:
            self.zoom_out.stop()

    def toggle_move_left(self, key_down):
        if key_down:
            if not self.move_left.running:
                self.move_left.start()
        else:
            self.move_left.stop()

    def toggle_move_right(self, key_down):
        if key_down:
            if not self.move_right.running:
                self.move_right.start()
        else:
            self.move_right.stop()

    def toggle_move_up(self, key_down):
        if key_down:
            if not self.move_up.running:
                self.move_up.start()
        else:
            self.move_up.stop()

    def toggle_move_down(self, key_down):
        if key_down:
            if not self.move_down.running:
                self.move_down.start()
        else:
            self.move_down.stop()
