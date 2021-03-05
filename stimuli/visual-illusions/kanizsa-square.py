#! /usr/bin/env python
# Time-stamp: <2021-03-04 11:51:30 christophe@pallier.org>

""" Display Kanisza illusory square

(see https://openi.nlm.nih.gov/detailedresult?img=PMC4211395_fnhum-08-00854-g0001&req=4 )

"""

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# create graphic window
W, H = 500, 500  # size (width and height) of the graphic window
# (0,0) is at the upper left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
pygame.display.set_caption('Kanisza square')

screen.fill(GRAY)

# size of the rectangle
width, height = 200, 200

# coordinate of the corners of the rectangle,
# which are also that of the centers of the circles
left = center_x - width // 2
right = center_x + width // 2
top = center_y - height // 2
bottom = center_y + height // 2

# draw circles
radius = 50
pygame.draw.circle(screen, BLACK, (left, top), radius, 0)
pygame.draw.circle(screen, BLACK, (right, top), radius, 0)
pygame.draw.circle(screen, WHITE, (left, bottom), radius, 0)
pygame.draw.circle(screen, WHITE, (right, bottom), radius, 0)

# draw the rectangle
pygame.draw.rect(screen, GRAY, (left, top, width, height))

# switch the backbuffer to display the figure
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "kanizsa-square.png")

# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()
