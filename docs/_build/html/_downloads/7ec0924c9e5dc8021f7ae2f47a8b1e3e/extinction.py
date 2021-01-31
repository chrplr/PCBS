#! /usr/bin/env python
# Time-stamp: <2019-03-10 10:25:57 christophe@pallier.org>

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

l = 50  # square side length
e = 8  # space between squares
n = 20  # number of columns and rows

W, H = n * (l + e) + e, n * (l + e) + e  # graphic window size

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(GRAY)

# Create a rectangle https://www.pygame.org/docs/ref/rect.html

for row in range(n):
    for col in range(n):
        left, top = e + col * (l + e), e + row * (l + e)
        myrect = pygame.Rect(left, top, l, l)
        pygame.draw.rect(screen, BLACK, myrect)
        pygame.draw.circle(screen, WHITE, (left - e//2, top - e//2), e//2)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "extinction-grid.png")

# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

