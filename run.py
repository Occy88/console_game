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

# import keyboard
WITH_KEYBOARD = False
import math

screen = curses.initscr()
curses.noecho()
screen.keypad(True)
print("starting")


def main(screen):
    # Clear screen
    # exit(0)
    world_plane = Plane(Vector(0, 0), Vector(1, 1))
    keyboard_handler = Keyboard(screen)
    screen.clear()
    screen2 = Screen(100, 40,0, 0, Vector(1, 0.46))
    game_camera = Camera(Vector(30,30),Vector(1,1), screen2)
    game_time = time.time()
    print("INITIATION SUCCESSFUL")
    keyboard_handler.on_press(game_camera.key_down)
    keyboard_handler.on_release(game_camera.key_up)
    i = 0
    while True:
        i += 1
        # print(i)
        # screen.clear()
        # screen2.write_str(Vector(0,5),str(i))
        game_camera.update()
        square_origin = Vector(30, 30)
        square_length = Vector(10,10)
        # game_camera.view_plane.origin=square_origin
        # 0,0 -> 10,10 -> 52,20
        world_plane.transform_to_plane(square_origin, game_camera.view_plane)
        world_plane.transform_by_ratio(square_origin, game_camera.view_plane)
        world_plane.transform_by_ratio(square_length, game_camera.view_plane)
        game_camera.view_plane.center_to_plane(square_origin,screen2.display_plane)
        # game_camera.view_plane.transform_by_ratio(square_length,screen2.display_plane)
        # screen2.display_plane.transform_to_plane(square_origin, screen_plane)
        # screen2.display_plane.transform_by_ratio(square_length, screen_plane)
        screen2.write_str(Vector(0,-1),game_camera.view_plane.origin.__str__()+game_camera.view_plane.dim.__str__())

        screen2.write_str(Vector(0,-2),square_length.__str__()+square_origin.__str__())

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
        screen2.draw_shape(lines)
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
