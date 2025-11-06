#! /usr/bin/env python
# Time-stamp: <2021-02-25 21:43:23 christophe@pallier.org>

""" Illusory Line-motion demo.
"""

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

W, H = 800, 500  # window size

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(BLACK)

def ilm(direction):
    assert direction in ['left', 'right']

    width, height = 120, 40  # size of the rectangle
    # Note: the square has size height * height

    top = H // 2 - 100      
    left = W // 2 - width // 2   # position of (left side of) the rectangle

    rectangle = pygame.Rect(left, top, width, height)

    if direction == 'right':
        xsquare_coord = left
    else:  # directon must be left 
        xsquare_coord = left + width - height

    square = pygame.Rect(xsquare_coord, top, height, height)
    
    # preparation phase
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (W // 2, H // 2), 5) # display a fixation point
    pygame.display.flip()
    pygame.time.wait(1500)

    # cue
    pygame.draw.circle(screen, WHITE, (W // 2, H // 2), 5)
    pygame.draw.rect(screen, WHITE, square)
    pygame.display.flip()
    pygame.time.wait(20)

    # rectangle
    pygame.draw.circle(screen, WHITE, (W // 2, H // 2), 5)
    pygame.draw.rect(screen, WHITE, rectangle)
    pygame.display.flip()
    pygame.time.wait(1000)

    # clear the screen
    screen.fill(BLACK)
    pygame.display.flip()


for dir in ['left', 'left', 'left', 'right', 'right', 'right']:
    ilm(dir)


pygame.quit()
