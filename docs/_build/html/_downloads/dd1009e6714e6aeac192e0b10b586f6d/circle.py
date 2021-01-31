#! /usr/bin/env python
# Time-stamp: <2019-03-09 09:45:17 christophe@pallier.org>

""" Draw a circle using pygame (see <http://www.pygame.org>). """

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 500, 500  # graphic window size

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle
pygame.draw.circle(screen, RED, (W // 2, H // 2), 100, 0)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "circle-red.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
