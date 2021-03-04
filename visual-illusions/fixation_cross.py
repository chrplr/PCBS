#! /usr/bin/env python
# Time-stamp: <2021-03-04 12:15:50 christophe@pallier.org>
""" Display a fixation cross.

   See:
   - `Pygame drawing basics <https://www.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/>`__
   - `Pygame's online documentation <https://www.pygame.org/docs/>`

"""

import pygame


def draw_fixation_cross(x, y, length=20, width=5, color=pygame.Color('black')):
    pygame.draw.line(screen, color, (x, y - length), (x, y + length), width)
    pygame.draw.line(screen, color, (x - length, y), (x + length, y), width)


if __name__ == '__main__':
    pygame.init()

    #  create the window
    W, H = 500, 500  # Size of the graphic window
    center_x = W // 2
    center_y = H // 2
    screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
    pygame.display.set_caption('Fixation cross')
    screen.fill(pygame.Color('white')) 

    draw_fixation_cross(center_x, center_y)

    pygame.display.flip()  # display the backbuffer on the screen

    # save the image into a file
    pygame.image.save(screen, "fixation-cross.png")

    # Wait until the window is closed
    quit_button_pressed = False
    while not quit_button_pressed:
        pygame.time.wait(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_button_pressed = True

    pygame.quit()
