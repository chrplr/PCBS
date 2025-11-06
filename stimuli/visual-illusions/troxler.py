#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:29:18 christophe@pallier.org>

""" Display a the Troxler figure.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

# Colors are triplets containint RGB values
# see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# found with https://www.google.com/search?q=color+picker
YELLOW = (252, 251, 210)
GREEN = (222, 252, 189)
BLUE = (189, 252, 251)
ROSE = (250, 217, 248)

W, H = 800, 800  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

center_x = W // 2
center_y = H // 2

#  create the window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Troxler illusion')
screen.fill(WHITE)

# fixation point:
pygame.draw.circle(screen, BLACK, (center_x, center_y), 5)

radius = 40
coord = 300

x1 = center_x - coord
x2 = center_x
x3 = center_x + coord
y1 = center_y - coord
y2 = center_y
y3 = center_y + coord

pygame.draw.circle(screen, BLUE,   (x1, y1), radius)
pygame.draw.circle(screen, ROSE,   (x2, y1), radius)
pygame.draw.circle(screen, YELLOW, (x3, y1), radius)
pygame.draw.circle(screen, GREEN,  (x1, y2), radius)
pygame.draw.circle(screen, BLUE,   (x3, y2), radius)
pygame.draw.circle(screen, ROSE,   (x1, y3), radius)
pygame.draw.circle(screen, YELLOW, (x2, y3), radius)
pygame.draw.circle(screen, GREEN,  (x3, y3), radius)


pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "troxler.png")

# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
