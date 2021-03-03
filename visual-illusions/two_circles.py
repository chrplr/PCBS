#! /usr/bin/env python
# Time-stamp: <2021-03-03 10:42:32 christophe@pallier.org>

""" Display two circles side by side.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

# Colors are triplets containint RGB values
# see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#  create the window
W, H = 500, 500  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)

screen.fill(WHITE)  # fill it with white

# draw circles
radius = 100
horiz_shift = 120  # x position relative to center
pygame.draw.circle(screen, RED, (center_x - horiz_shift, center_y), 100, 0)
pygame.draw.circle(screen, BLUE, (center_y + horiz_shift, center_y), 100, 0)

pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "two-circles.png")

# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
