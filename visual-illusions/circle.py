#! /usr/bin/env python
# Time-stamp: <2021-02-24 10:53:16 christophe@pallier.org>

""" Display a circle.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

# Colors are triplets containint RGB values (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 500, 500  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

#  create the window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)

screen.fill(WHITE)  #  fill it with white

# Draw a rectangle
width, height = 200, 200
pygame.draw.circle(screen, RED, (W // 2, H // 2), 100, 0)

pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "circle-red.png")

# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
