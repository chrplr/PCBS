#! /usr/bin/env python
# Time-stamp: <2018-10-04 07:23:37 cp983411>

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 500, 500  # graphic window size

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)

# Create a rectangle https://www.pygame.org/docs/ref/rect.html
width, height = 200, 200
left, top = (W-width)/2, (H-height)/2 # (0,0) is at the upper left hand corner of the screen.
myrect = pygame.Rect(left, top, width, height)
pygame.draw.rect(screen, BLUE, myrect)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "square-blue.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

