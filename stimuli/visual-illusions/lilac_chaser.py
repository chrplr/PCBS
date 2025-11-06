#! /usr/bin/env python
# Time-stamp: <2021-03-04 14:17:15 christophe@pallier.org>
""" Display the Lilac Chaser.

See <https://en.wikipedia.org/wiki/Lilac_chaser>
"""

from math import sin, cos, pi
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

W, H = 800, 800  # Size of the graphic window
center_x = W // 2
center_y = H // 2

n = 12  # number of circles
radius = 40  # radius of circles
distance = 300  # distance of circles from fixation point (window's center)
ROSE = (250, 217, 248)  # color of circles

#  create the window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Lilac Chaser')

current_pos = 0
done = False
while not done:  # loops until the Quit button is pressed
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
            pygame.draw.circle(screen, WHITE, (x, y), radius)
        else:
            pygame.draw.circle(screen, ROSE, (x, y), radius)

    pygame.display.flip()  # display the backbuffer
    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    current_pos = (current_pos + 1) % n

pygame.quit()
