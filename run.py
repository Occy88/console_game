import time
import curses
from curses import wrapper
from Tools.Camera import Camera
from Utils.Vector import Vector
import threading
from Utils.Keyboard import Keyboard
import keyboard
from Tools.Screen import Screen
from Utils.Plane import Plane
import os
from Tools.ImageToAscii import get_char, grey_scale, scale
import numpy as np

root = os.getcwd()
# from Tools.ImageToAscii import convert_image

# import keyboard
WITH_KEYBOARD = False
import math

t = time.time()
from PIL import Image
import psutil

# LOAD IMAGE
image = Image.open('Tools/im1.jpg')
image = grey_scale(image)
image.rotate(180)
#
# import time
#
# t = time.time()
#

screen = curses.initscr()
curses.noecho()
screen.keypad(True)

print("starting")


def main(screen):
    global image
    # Clear screen
    # exit(0)
    world_plane = Plane(Vector(0, 0), Vector(1, 1))
    keyboard_handler = Keyboard(screen)
    screen.clear()
    screen2 = Screen(100, 40, 0, 0, Vector(1, 0.46))
    game_camera = Camera(Vector(30, 30), Vector(1, 1), screen2)
    game_time = time.time()
    print("INITIATION SUCCESSFUL")
    keyboard_handler.on_press(game_camera.key_down)
    keyboard_handler.on_release(game_camera.key_up)

    i = 0
    square_origin_t = Vector(30, 30)
    square_length_t = Vector(150, 180)
    t = time.time()

    vel = Vector(0,0)
    while True:
        # game_camera.view_plane.origin=square_origin_t.copy()
        i += 1
        # print(i)
        # screen.clear()
        # screen2.write_str(Vector(0,5),str(i))
        # game_camera.view_plane.origin=Vector(-50,-150)
        t_el = time.time() - t
        square_origin_t.add(vel.copy().multiply(t_el))
        t = time.time()
        game_camera.update()
        square_origin = square_origin_t.copy()
        square_length = square_length_t.copy()
        # game_camera.view_plane.origin=square_origin
        # 0,0 -> 10,10 -> 52,20
        world_plane.transform_to_plane(square_origin, game_camera.view_plane)
        world_plane.transform_by_ratio(square_origin, game_camera.view_plane)
        world_plane.transform_by_ratio(square_length, game_camera.view_plane)
        game_camera.view_plane.center_to_plane(square_origin, screen2.display_plane)
        # game_camera.view_plane.transform_by_ratio(square_length,screen2.display_plane)
        # screen2.display_plane.transform_to_plane(square_origin, screen_plane)
        # screen2.display_plane.transform_by_ratio(square_length, screen_plane)
        screen2.write_str(Vector(0, -1), game_camera.view_plane.origin.__str__() + game_camera.view_plane.dim.__str__())

        screen2.write_str(Vector(0, -2), square_origin.__str__())

        # print(square_origin)
        # print(world_plane.origin)
        # print(game_camera.view_plane.origin)
        #
        # print(screen2.display_plane.origin)
        lines = []
        start = square_origin.copy().subtract(square_origin.copy().divide(2))
        lines.append(start.copy().add(Vector(0, 0).multiply_vector(square_length)))
        lines.append(start.copy().add(Vector(1, 0).multiply_vector(square_length)))
        lines.append(start.copy().add(Vector(1, 1).multiply_vector(square_length)))
        lines.append(start.copy().add(Vector(0, 1).multiply_vector(square_length)))
        lines.append(start.copy().add(Vector(0, 0).multiply_vector(square_length)))

        screen2.scale_to_screen(lines)
        # screen2.draw_shape(lines)
        im_size = square_length.copy()
        screen2.scale_to_screen([im_size])
        im = scale(image, (int(im_size.x), int(im_size.y)))

        im_pos = start.copy()
        max_x, max_y = im.size
        arr = []
        init_pos=im_pos
        # init_pos=Vector(0,-50)
        for y in range(max_y):
            # to_write = ''
            for x in range(max_x):
                # to_write += get_char(im, (x, y))
                char = get_char(im, (x, y))
                pos = init_pos.copy().add(Vector(x, y))
                screen2.write_str(pos, char)
            # screen2.refresh()

            # screen2.write_str(Vector(0, -3),image_loc.y+max_y-yto_write)
            # screen2.write_str(Vector(0, -4), to_write)
            # screen2.write_str(Vector(image_loc.x, image_loc.y + (max_y - y)), to_write)
        screen2.write_str(Vector(0, -5), init_pos.__str__())

        screen.refresh()
        screen2.refresh()

        # screen2.write_str(Vector(3, 3),
        #                   game_camera.view_plane.origin.getP().__str__() + game_camera.view_plane.dim.getP().__str__())

        time.sleep(.1)
        game_time = time.time()

        # screen.clear()
        # y, x = screen.getmaxyx()
        # i=-10
        # print('YO')
        # print(screen.getmaxyx())
        # screen.addstr(10,10,'hello')
        # screen.refresh()
        # while True:
        #     i+=1
        #     # Check if screen was re-sized (True or False)
        #     resize = curses.is_term_resized(y, x)
        #
        #     # Action in loop if resize is True:
        #     if resize is True:
        #         y, x = screen.getmaxyx()
        #         screen.clear()
        #         curses.resizeterm(y, x)
        #         screen.refresh()
        #     screen.addstr(10, 10, 'hello: ' + x.__str__() + ':' + y.__str__())
        #
        #     time.sleep(0.5)
        #     if i>10:
        #         break
        #
        # # This raises ZeroDivisionError when i == 10.
        # for i in range(0, 11):
        #     v = i - 10
        #     screen.addstr(i, 0, '10 divided by {} is {}'.format(v, 10 / v))
        #
        # screen.refresh()
        # screen.getkey()


if __name__ == '__main__':
    print("STARTING")
wrapper(main)
# terminate
print("BYE")
screen.keypad(False)
curses.echo()
curses.endwin()
