#! /usr/bin/env python
# Time-stamp: <2019-10-24 15:56:55 christophe@pallier.org>

""" Draw a circle using pygame (see <http://www.pygame.org>). """

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

W, H = 500, 500  # graphic window size

pygame.init()
screen = pygame.display.set_mode((H, W), pygame.DOUBLEBUF)

for _ in range(10):
        screen.fill(WHITE)
        pygame.draw.circle(screen, RED, (W // 2, H // 2), 10, 0)
        pygame.display.flip()
        t0 = pygame.time.get_ticks()
        pygame.event.clear()

        pygame.event.wait()

        t1 = pygame.time.get_ticks()
        screen.fill(WHITE)
        pygame.display.flip()

        print(t1-t0)
        pygame.time.wait(2000)



