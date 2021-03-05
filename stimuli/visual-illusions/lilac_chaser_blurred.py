#! /usr/bin/env python
# Time-stamp: <2021-03-04 14:22:36 christophe@pallier.org>
""" Display the Lilac Chaser.

See <https://en.wikipedia.org/wiki/Lilac_chaser>

Note: this script requires the image file ``blurred_disk.png`` whic can downloaded from https://github.com/chrplr/PCBS/tree/master/visual-illusions
"""

from math import sin, cos, pi
import pygame

WHITE = pygame.Color('white')
BLACK = pygame.Color('black')

W, H = 1000, 1000  # Size of the graphic window
center_x = W // 2
center_y = H // 2

n = 12  # number of circles
radius = 40  # radius of circles
distance = 300  # distance of circles from fixation point (window's center)

#  create the window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Lilac Chaser Blurred')

disk = pygame.image.load('blurred_disk.png')
w, h = disk.get_size()
mask = pygame.Surface((w, h))
mask.fill(WHITE)

current_pos = 0
quit_button_pressed = False
while not quit_button_pressed:
    screen.fill(WHITE)
    # fixation cross:
    length = 20
    width = 5
    x = center_x
    y = center_y
    pygame.draw.line(screen, BLACK, (x, y - length), (x, y + length), width)
    pygame.draw.line(screen, BLACK, (x - length, y), (x + length, y), width)

    for k in range(n):
        x = center_x + int(distance * cos(2 * pi * k / n))
        y = center_y + int(distance * sin(2 * pi * k / n))
        if k == current_pos:
            screen.blit(mask, (x - w // 2, y - h // 2))
        else:
            screen.blit(disk, (x - w // 2, y - h // 2))

    pygame.display.flip()  # display the backbuffer
    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

    current_pos = (current_pos + 1) % n

pygame.quit()
