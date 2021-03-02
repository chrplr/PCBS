#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:34:13 christophe@pallier.org>

""" Hering illusion demo.

    See https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/
"""

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

W, H = 1000, 700  # Size of the graphic window

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Hering illusion')

screen.fill(WHITE)  # fill the window with white

# two vertical lines
pygame.draw.line(screen, RED, (W // 2 - 60, 0), (W // 2 - 60, H), 3)
pygame.draw.line(screen, RED, (W // 2 + 60, 0), (W // 2 + 60, H), 3)

pygame.display.flip()  # display the backbuffer

pygame.time.wait(2000)

pygame.draw.line(screen, RED, (W // 2 - 60, 0), (W // 2 - 60, H), 3)
pygame.draw.line(screen, RED, (W // 2 + 60, 0), (W // 2 + 60, H), 3)
# background black lines
for x in range(-W // 3, 4 * W // 3, 30):
    pygame.draw.line(screen, BLACK, (x, 0), (W - x, H), 1)

pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "hering.png")


# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
