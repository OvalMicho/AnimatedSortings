import pygame
from random import randint
import csv
from time import sleep
from copy import deepcopy
from constants import *
# from load_func import *

#constants

FPS = 100

WIDTH = 604
HEIGHT = 510


# lst = list(range(100))
arr = []
ist = iter(arr)


def open_csv(way):
    arr = []
    with open(way) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            arr.append([int(i) for i in row])
    return arr


def update_list(ist, shift=1):
    # return lst[-shift:] + lst[:-shift]
    # return [randint(0, 100) for i in range(100)]
    try:
        return next(ist)
    except Exception:
        # 5
        sleep(5)
        return None


def make_colour(max_el, min_el, elem):
    pc = (elem - min_el) / (max_el - min_el)
    return int(pc * 255), int((1 - pc) * 255), 0


# flag cam be color 'c' or height 'h' or 'hc'
def draw_all(screen, lst, flag='h'):
    x = 2
    d_x = (WIDTH - 1) // len(lst)
    one_h = (HEIGHT - 10) // max(lst)
    max_el, min_el = max(lst), min(lst)
    if flag == 'h':
        for elem in lst:
            pygame.draw.rect(screen, "#ff8c69", (x, HEIGHT - one_h * elem, d_x - 1, one_h * elem))
            # pygame.draw.circle(screen, (255, 0, 0), (x, HEIGHT - one_h * elem), 3, 2)
            # pygame.draw.circle(screen, (0, 0, 255), (x + d_x, HEIGHT), 3, 2)
            x += d_x

    elif flag == 'c':
        for elem in lst:
            pygame.draw.rect(screen, make_colour(max_el, min_el, elem), (x, 0, d_x, HEIGHT))
            x += d_x

    elif flag == 'hc':
        for elem in lst:
            pygame.draw.rect(screen, make_colour(max_el, min_el, elem),
                             (x, HEIGHT - one_h * elem, d_x, one_h * elem))
            x += d_x


if __name__ == '__main__':
    pygame.init()
    size = width, height = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    arr = open_csv('shell_sort_data.csv')
    ist = iter(arr)
    lst = update_list(ist)
    clock = pygame.time.Clock()
    run = True
    stop = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    break
                elif event.key == pygame.K_SPACE:
                    stop = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    stop = False

        if not stop:
            draw_all(screen, lst, flag='h')
            lst = update_list(ist)
            if not lst:
                ist = iter(arr)
                lst = update_list(ist)
            clock.tick(FPS)
            pygame.display.flip()
            screen.fill((0, 0, 0))












#load_func

import sys
import os
import pygame


def load_image(name, name_p, colorkey=None):
    fullname = os.path.join(name_p, name)
    # если файл не существует, то выходим
    try:
        assert os.path.isfile(fullname)
    except AssertionError:
        print(fullname)
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image