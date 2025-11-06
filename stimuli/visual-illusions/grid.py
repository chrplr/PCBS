#! /usr/bin/env python
# Time-stamp: <2021-03-03 10:39:36 christophe@pallier.org>

""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# parameters of the grid
n_rows, n_cols = 10, 10
cell_side_length = 50
space_between_cells = 10
margin = 30  # borders size
square_color = BLACK
background_color = WHITE

# graphic window cell_side_length
W = n_cols * cell_side_length + (n_cols - 1) * space_between_cells + 2 * margin
H = n_rows * cell_side_length + (n_rows - 1) * space_between_cells + 2 * margin

# creation of the graphics window
pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Herman Grid')

screen.fill(background_color)

# construction of the grid
for i_row in range(n_rows):
    for i_col in range(n_cols):
        x_left = margin + i_col * (cell_side_length + space_between_cells)
        y_top = margin + i_row * (cell_side_length + space_between_cells)
        pygame.draw.rect(screen,
                         square_color,
                         (x_left, y_top, cell_side_length, cell_side_length))

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "grid.png")

# wait till the window is closed
done = False
while not done:
    pygame.time.wait(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
