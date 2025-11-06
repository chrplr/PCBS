#! /usr/bin/env python
# Time-stamp: <2019-03-09 09:54:21 christophe@pallier.org>

""" Draw a triangle using pygame (see <http://www.pygame.org>). """

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

W, H = 500, 500  # graphic window size

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines
size = 60
point1 = W//2 - size, H//2 + size
point2 = W//2 + size, H//2 + size
point3 = W//2, H//2 - size
pygame.draw.lines(screen, BLACK, True, (point1, point2, point3), 5)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "triangle-black.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
