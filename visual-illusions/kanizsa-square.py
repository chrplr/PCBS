#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:28:59 christophe@pallier.org>

""" Display Kanisza illusory square

(see https://openi.nlm.nih.gov/detailedresult?img=PMC4211395_fnhum-08-00854-g0001&req=4 )

"""

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create graphic window
W, H = 500, 500  # size (width and height) of the graphic window
# (0,0) is at the upper left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
pygame.display.set_caption('Kanisza illusory contours')

screen.fill(GRAY)

# size of the rectangle
width, height = 200, 200

# coordinate of the corners of the rectangle,
# which are also that of the centers of the circles
left = center_x - width // 2
right = center_x + width // 2
top = center_y - height // 2
bottom = center_y + height // 2

radius = 50
pygame.draw.circle(screen, BLACK, (left, top), radius, 0)
pygame.draw.circle(screen, BLACK, (right, top), radius, 0)
pygame.draw.circle(screen, WHITE, (left, bottom), radius, 0)
pygame.draw.circle(screen, WHITE, (right, bottom), radius, 0)

myrect = pygame.Rect(left, top, width, height)
pygame.draw.rect(screen, GRAY, myrect)

# switch the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "kanizsa-square.png")

# wait till the window is closed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
