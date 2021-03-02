#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:27:46 christophe@pallier.org>

""" Display a square.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

# Colors are triplets containint RGB values
# (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  create the window
W, H = 500, 500  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('square')

screen.fill(WHITE)  # fill it with white

# Draw a rectangle
width, height = 200, 200  # dimensions of the rectangle in pixels
left = center_x - width // 2  # x coordinates of topleft corner
top = center_y - height // 2  # y coordinate of topleft corner
pygame.draw.rect(screen, BLUE, (left, top, width, height))

pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "square-blue.png")

# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
