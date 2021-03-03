#! /usr/bin/env python
# Time-stamp: <2021-03-03 10:46:23 christophe@pallier.org>
""" Draw a triangle using pygame (see <http://www.pygame.org>). """

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

W, H = 500, 500  # graphic window size
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
pygame.display.set_caption('triangle')
screen.fill(WHITE)

# https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines
size = 60
point1 = (center_x - size, center_y + size)
point2 = (center_x + size, center_y + size)
point3 = (center_x, center_y - size)
pygame.draw.lines(screen, BLACK, True, (point1, point2, point3), 5)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "triangle-black.png")

# wait till the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
