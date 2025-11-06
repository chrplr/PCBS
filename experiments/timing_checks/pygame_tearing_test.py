#! /usr/bin/env python
# Time-stamp: <2022-05-14 15:04:33 christophe@pallier.org>

""" Tearing test. Displays a vertical moving bar to check the absence (or presence) of tearing.
If the synchronization to vertical blank is set and the computer is fast enough, 
the bar should not be broken
"""

from collections import Counter
import pygame

OPENGL = True  # should be true to get blocking on vblank by display.flip()
BACKGROUND_COLOR = (127, 127, 127)
BAR_COLOR = (255, 255, 255)

pygame.init()

if OPENGL:
    flags = pygame.OPENGL | pygame.SCALED | pygame.DOUBLEBUF | pygame.FULLSCREEN
else:
    flags = pygame.DOUBLEBUF | pygame.FULLSCREEN

W, H = pygame.display.get_desktop_sizes()[0]  # current screen resolution
screen = pygame.display.set_mode((W, H), flags, vsync=1)

pygame.time.wait(1000)

t0 = pygame.time.get_ticks()
timings= []
for skip in [8, 16, 32]:
    xpos = 0
    while xpos < W:
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, BAR_COLOR, (xpos, 0, skip, H))
        pygame.display.flip()
        t1 = pygame.time.get_ticks()
        timings.append(t1 - t0)
        xpos += skip
        t0 = t1


pygame.quit()

print('histogram of time differences between displays')
print(Counter(timings))
