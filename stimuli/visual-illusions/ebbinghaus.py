#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:27:09 christophe@pallier.org>

"""Draws the Ebbinghaus-Titchener illusion.

See https://en.wikipedia.org/wiki/Ebbinghaus_illusion

"""

import pygame  # see www.pygame.org
from math import sin, cos, pi

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)


def Ebbinghaus(surface, n, d, r1, r2, col1, col2, x, y):
    """ Draws a circle surrounded by outer ones.

        Args:
            surface: pygame surface to display the stimulus on
            n: number of peripheral, outer circles
            d: distance between the center of inner circle and peripheral ones
            r1: radius of inner circle
            r2: radius of outer circles
            col1: color of the inner circle
            col2: color of the outer circles
            x, y: coordinates of the center of the figure on the screen
        Returns:

        None
            the stimulus is drawn on the surface

    """

    border_size = 2
    # draw inner circle
    pygame.draw.circle(surface, col1, (x, y), r1, border_size)
    # draw peripheral circles
    for i_circle in range(n):
        angle = (2 * pi * i_circle) / n
        x1 = x + int(d * cos(angle))
        y1 = y + int(d * sin(angle))
        pygame.draw.circle(surface, col2, (x1, y1), r2, border_size)


W, H = 700, 500  # graphic window size

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Ebbinghaus illusion')
screen.fill(WHITE)

Ebbinghaus(screen, 8, 100, 25, 35, BLACK, BLACK, W//2 + 150, H//2)
Ebbinghaus(screen, 12, 80, 25, 15, BLACK, BLACK, W//2 - 150, H//2)

pygame.display.flip()
pygame.image.save(screen, "ebbinghaus.png")

# wait till the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
