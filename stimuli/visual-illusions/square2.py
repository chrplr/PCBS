#! /usr/bin/env python
# Time-stamp: <2019-10-24 14:50:38 christophe@pallier.org>

""" Display a square using [pygame](http://www.pygame.org).

For a quick introduction on drawing with pygame,
see <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>
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

W, H = 500, 500  # graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

# open the window and fill it with white
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)


# Create a rectangle (see )<https://www.pygame.org/docs/ref/rect.html>)
width, height = 20, 20
left, top = (W - width) // 2, (H-400) // 2
myrect = pygame.Rect(left, top, width, height)
pygame.draw.rect(screen, BLUE, myrect)

# display the backbuffer
pygame.display.flip()

pygame.time.wait(500)

width, height = 20, 80
left, top = (W - width) // 2, (H-400) // 2
myrect = pygame.Rect(left, top, width, height)
pygame.draw.rect(screen, BLUE, myrect)

# display the backbuffer
pygame.display.flip()

pygame.time.wait(500)

screen.fill(WHITE)
pygame.display.flip()

pygame.time.wait(1000)

# wait till the window is closed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True

