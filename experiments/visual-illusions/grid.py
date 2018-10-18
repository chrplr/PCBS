#! /usr/bin/env python
# Time-stamp: <2018-10-04 07:23:37 cp983411>

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

l = 50  # square side length
e = 10  # space between squares
n = 10  # number of columns and rows

W, H = n * (l + e) + e, n * (l + e) + e  # graphic window size

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(WHITE)

# Create a rectangle https://www.pygame.org/docs/ref/rect.html

for row in range(n):
    for col in range(n):
        left, top = e + col * (l + e), e + row * (l + e)
        myrect = pygame.Rect(left, top, l, l)
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

