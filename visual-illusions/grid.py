#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:32:17 christophe@pallier.org>

""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

n_rows, n_cols = 10, 10  # number of squares per row and column
size = 50  # square size (length of)side in pixels)
margin = 10  # space between squares

# graphic window size
W = n_cols * (size + margin) + margin
H = n_rows * (size + margin) + margin

# creation of the graphics window
pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
pygame.display.set_caption('Herman Grid')

screen.fill(WHITE)

# construction of the grid
for row in range(n_rows):
    for col in range(n_cols):
        left = margin + col * (size + margin)
        top = margin + row * (size + margin)
        pygame.draw.rect(screen, BLACK, (left, top, size, size))

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
