#! /usr/bin/env python
# Time-stamp: <>

"""Line-motion illusion.

"""

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
W, H = 500, 500
width, height = 20, 20

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# Create two rectangle https://www.pygame.org/docs/ref/rect.html

left, top = (W-width)/2, (H-height)/2 # (0,0) is at the upper left hand corner of the screen.
mysquare = pygame.Rect(left, top, width, height)
myrect = pygame.Rect(left, top, width, height * 3)

# loops till the window is closed
done = False
while not done:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, mysquare)
    pygame.display.flip()
    pygame.time.wait(200)

    pygame.draw.rect(screen, BLACK, myrect)
    pygame.display.flip()
    pygame.time.wait(500)

    screen.fill(WHITE)
    pygame.display.flip()

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

pygame.quit()
