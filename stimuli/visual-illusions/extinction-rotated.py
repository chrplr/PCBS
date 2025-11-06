#! /usr/bin/env python3
# Time-stamp: <2021-03-02 12:12:53 christophe@pallier.org>

import pygame  # see www.pygame.org

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

side = 200  # square side length
gap = 20  # space between squares
radius = int(gap / 1.414)  # radius of the circles
n = 7  # number of columns and rows of squares

# graphic window size
W = n * (side + gap) + gap
H = W

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)

# construction of an horizontal grid on a surface ('canvas')
# we need a area to draw on, because of the rotation
canvas = pygame.Surface((2 * H, 2 * W))
canvas.fill(GRAY)

for row in range(2 * n):
    for col in range(2 * n):
        left = gap + col * (side + gap)
        top = gap + row * (side + gap)
        pygame.draw.rect(canvas, BLACK, (left, top, side, side))
        pygame.draw.circle(canvas, WHITE,
                           (left - gap//2, top - gap//2),
                           int(gap/1.414))

# Rotation of the canvas at an angle of 45°
rot_image = pygame.transform.rotate(canvas, 45)
screen.fill(WHITE)
screen.blit(rot_image, (-W, -H))

# display the backbuffer
pygame.display.flip()

# save the image into a file
pygame.image.save(screen, "extinction-grid-rotated.png")

# wait till the window is closed
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
