#!/usr/bin/env python
# Time-stamp: <2021-03-02 22:06:31 christophe@pallier.org>

""" Moving square using pygame """

import pygame

# Colors are triplets containint RGB values
# see <https://www.rapidtables.com/web/color/RGB_Color.html>
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#  create the graphic window
pygame.init()
W, H = 800, 800  # Size of the graphic window 
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('moving square') 
screen.fill(WHITE)  # fill it with white

# Draw a rectangle
width, height = 20, 20
y = (H - height) // 2

wait_time = 20  # number of ms between each step
step = 10  # number of pixels to move
x = 50  # starting abscissa

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
