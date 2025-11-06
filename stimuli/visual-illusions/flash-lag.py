#! /usr/bin/env python
# Time-stamp: <2021-03-02 15:15:49 christophe@pallier.org>

""" Flash-lag illusion. """

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# graphic window size
W, H = 800, 400
center_x = W // 2
center_y = H // 2

# create the graphic window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Flash-lag illusion')
screen.fill(WHITE)

# size and starting position of the moving square
width, height = 20, 20
x = width
y = center_y - 2 * height

# number of pixels to skip at each loop
speed = 10

# loops till the window is closed
close_event_received = False
while not close_event_received:
    screen.fill(WHITE)
    # draw moving square
    pygame.draw.rect(screen, BLACK, (x, y, width, height))
    # flash fixed square if moving square is centered
    if abs(x - width // 2 - center_x) < (width // 2):
        pygame.draw.rect(screen, BLACK, (x, y + 2 * height, width, height))

    pygame.display.flip()
    pygame.time.wait(30)  # the actual duration may vary
                          # (waiting on vsync or not)

    if (x < width) or (x > (W - 2 * width)):
        speed = - speed  # bouncing
    x = x + speed

    # check if user asked to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_event_received = True

pygame.quit()
