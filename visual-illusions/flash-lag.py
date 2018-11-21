#! /usr/bin/env python
# Time-stamp: <2018-10-09 13:24:55 cp983411>

"""Flash-lag illusion.

"""

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
W, H = 800, 400
width, height = 20, 20

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
screen.fill(WHITE)

# Create two rectangle https://www.pygame.org/docs/ref/rect.html

left, top = (W-width)/2, (H-height)/2 # (0,0) is at the upper left hand corner of the screen.
mysquare1 = pygame.Rect(left - 300, top - 3 * height, width, height)
mysquare2 = pygame.Rect(left, top, width, height)


# loops till the window is closed
done = False
while not done:
    print(mysquare1.x)
    if mysquare1.x > int(0.8 * W):
        step = - 10
    if mysquare1.x < int(0.2 * W):
        step = 10
    mysquare1 = mysquare1.move(step, 0)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, mysquare1)
    if abs(mysquare1.x - W//2) < 5:
           pygame.draw.rect(screen, BLACK, mysquare2)

    pygame.display.flip()
    pygame.time.wait(32)  # the actual duration may vary (waiting on vsync or not)

    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

pygame.quit()
