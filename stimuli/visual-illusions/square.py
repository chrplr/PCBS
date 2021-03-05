#! /usr/bin/env python
# Time-stamp: <2021-03-04 12:14:30 christophe@pallier.org>
""" Display a square.

   See:
   - `Pygame drawing basics <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__
   - `Pygame's online documentation <https://www.pygame.org/docs/>`

"""

import pygame

# Colors are triplets containint RGB values
# (see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  create the window
W, H = 500, 500  # Size of the graphic window
# Note that (0,0) is at the *upper* left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('square')

screen.fill(WHITE)  # fill it with white

# Draw a rectangle at the center of the screen (in the backbuffer)
width, height = 200, 200  # dimensions of the rectangle in pixels
left_x = center_x - width // 2  # x coordinate of topleft corner
top_y = center_y - height // 2  # y coordinate of topleft corner
pygame.draw.rect(screen, BLUE, (left_x, top_y, width, height))

pygame.display.flip()  # display the backbuffer on the screen

# save the image into a file
pygame.image.save(screen, "square-blue.png")


# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()
