#! /usr/bin/env python
# Time-stamp: <2019-03-09 13:41:19 christophe@pallier.org>

""" Display [Herman grid](https://en.wikipedia.org/wiki/Grid_illusion) """

import sys
import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

if len(sys.argv) < 4:
    print("Usage: " + sys.argv[0] + " nsquares  sizeofsquare  margin")
    print("nsquares is the number of squares per columns and row")
    print("sizeofsqaure is the length of the side of the squares in pixels")
    print("margin is the space between squares in pixels")
    sys.exit()
else:
    n = int(sys.argv[1])
    size = int(sys.argv[2])
    margin = int(sys.argv[3])

nrows, ncols = n, n  # number of sqaures per row and column

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

