#! /usr/bin/env python
# Time-stamp: <2021-03-04 11:54:07 Jean-Victor Steinlein>
""" Draw a triangle using pygame (see <http://www.pygame.org>). """

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

W, H = 500, 500  # graphic window size
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
pygame.display.set_caption('triangle')
screen.fill(WHITE)

# Draw 3 circles
size = 130
width, height = 50, 50
pygame.draw.circle(screen, GRAY,  (center_x + size, center_y - size + 40), 50, 0)
pygame.draw.circle(screen, GRAY,  (center_x - size, center_y - size + 40), 50, 0)
pygame.draw.circle(screen, GRAY,  (center_x, center_y + size + 40), 50, 0)

# Draw a triangle at the center of the window
# https://www.pygame.org/docs/ref/draw.html#pygame.draw.lines
size = 130
point1 = (center_x - size, center_y + size - 40)
point2 = (center_x + size, center_y + size - 40)
point3 = (center_x, center_y - size - 40)
pygame.draw.lines(screen, BLACK, True, (point1, point2, point3), 5)

# Draw opposite triangle
size = 130
point1 = (center_x + size, center_y - size + 40)
point2 = (center_x - size, center_y - size + 40)
point3 = (center_x, center_y + size + 40)
pygame.draw.polygon(screen, WHITE, (point1, point2, point3))

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "triangle-black.png")

# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()
