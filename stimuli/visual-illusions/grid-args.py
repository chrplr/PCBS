#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:02:11 christophe@pallier.org>

""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

import sys
import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

if len(sys.argv) == 4:
    print("Usage: " + sys.argv[0] + " nsquares  sizeofsquare  margin")
    print("'nsquares' is the number of squares per columns and row")
    print("'sizeofsquare' is the length of the side of the squares in pixels")
    print("'margin' is the space between squares in pixels")
    sys.exit()

n = int(sys.argv[1])
size = int(sys.argv[2])
margin = int(sys.argv[3])

n_rows, n_cols = n, n  # number of sqaures per row and column

# graphic window size
W = n_cols * (size + margin) + margin
H = n_rows * (size + margin) + margin

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# construct the grid
for row in range(n_rows):
    for col in range(n_cols):
        left = margin + col * (size + margin)
        top = margin + row * (size + margin)
        pygame.draw.rect(screen, BLACK, (left, top, size, size))

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, f"grid-{n}-{size}-{margin}.png")

# wait till the window is closed
done = False
while not done:
        pygame.time.wait(100)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

