#! /usr/bin/env python
# Time-stamp: <2019-03-09 09:35:53 christophe@pallier.org>

""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

nrows, ncols = 10, 10  # number of sqaures per row and column
size = 50  # square size (length of)side in pixels)
margin = 10  # space between squares

# graphic window size
W = ncols * (size + margin) + margin
H = nrows * (size + margin) + margin

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# construct the grid
for row in range(nrows):
    for col in range(ncols):
        left, top = margin + col * (size + margin), margin + row * (size + margin)
        myrect = pygame.Rect(left, top, size, size) # https://www.pygame.org/docs/ref/rect.html
        pygame.draw.rect(screen, BLACK, myrect)

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

