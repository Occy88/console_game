# Python code to convert an image to ASCII image.
import sys, random, argparse
import numpy as np
import PIL
import math

from PIL import Image

# gray scale level values from:
# http://paulbourke.net/dataformats/asciiart/

# 70 levels of gray
gscale1 = ("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ", (69.0 / 255.0) / 3)

# 10 levels of gray
gscale2 = ('@%#*+=-:. ', (9.0 / 255.0) / 3)


def grey_scale(image):
    image.convert('L')


def scale(image, size_tuple):
    image.thumbnail(size_tuple, PIL.Image.ANTIALIAS)


def get_char(image, xy):
    global gscale1, gscale2
    pixel = image.getpixel(xy)
    tot = pixel[0] + pixel[1] + pixel[2]
    return gscale1[0][int(gscale1[1] * tot)]


import os

image = Image.open('cropped-9.jpeg')
im_arr = []
get_char(image, (100, 100))

import time

scale(image, (700, 700))
# print(image)

max_x, max_y = image.size
for y in range(max_y):
    print('')
    for x in range(max_x):
        print(get_char(image, (x, y)), end='')
print(time.time() - t)
print(im_arr)
print("-----------------")
