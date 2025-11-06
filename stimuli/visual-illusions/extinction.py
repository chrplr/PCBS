#! /usr/bin/env python
# Time-stamp: <2021-03-02 12:13:29 christophe@pallier.org>

""" Extinction illusion """

import pygame  # see www.pygame.org

# parameters
side = 200  # square side length
gap = 20  # space between squares
radius = int(gap / 1.414)  # radius of the circles
n = 7  # number of columns and rows of squares

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)

# graphic window size
W = n * (side + gap) + gap
H = W

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)
screen.fill(GRAY)

# draw the squares
for row in range(n):
    for col in range(n):
        left = gap + col * (side + gap)
        top = gap + row * (side + gap)
        pygame.draw.rect(screen, BLACK, (left, top, side, side))

# draw the circles
for row in range(1, n):
    for col in range(1, n):
        left = gap + col * (side + gap)
        top = gap + row * (side + gap)
        pygame.draw.circle(screen, WHITE, (left - gap//2, top - gap//2), radius)

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, f"extinction-grid-{n}-{side}-{gap}.png")

# wait till the window is closed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
