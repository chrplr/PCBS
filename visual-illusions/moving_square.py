#!/usr/bin/env python
# Time-stamp: <2021-02-23 22:00:37 christophe@pallier.org>


""" Moving square using pygame """

import pygame

# Colors are triplets containint RGB values (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 800, 800  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

#  create the window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)

screen.fill(WHITE)  #  fill it with white

# Draw a rectangle
width, height = 20, 20
y = (H - height) // 2

step = 10  # number of pixels to move
wait_time = 20  # nnumber of ms between each step
x = 50  # starting abscisse

done = False
while not done:
    pygame.time.wait(wait_time)
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (x, y, width, height))
    pygame.display.flip()
    x = x + step
    if x < 0 or x + width > W:  # bouncing
        step = - step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
