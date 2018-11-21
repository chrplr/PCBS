#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Time-stamp: <2012-09-22 15:38 christophe@pallier.org>

"""A series of trials where a dot is presented and the user must click as quickly as possible on the mouse. Reaction times are measured and saved in a file."""

import pygame, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

NTRIALS = 10  # number of trials
OUTPUT_FILE = 'reaction_times.csv'

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mouse.set_visible(False)
r = screen.get_rect()
W, H = r.width, r.height

reaction_times = []

try:
    for t in range(NTRIALS):

        waiting_time = random.randint(1000, 2000)
        pygame.time.delay(waiting_time)
        pygame.event.clear()
        t0 = pygame.time.get_ticks()

        pygame.draw.circle(screen, WHITE, (W // 2, H // 2), 4)
        pygame.display.update()

        buttonpressed = False
        while not(buttonpressed):
            for ev in pygame.event.get():
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    t1 = pygame.time.get_ticks()
                    buttonpressed = True
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                    raise Exception()
        reaction_times.append(t1 - t0)

        screen.fill(BLACK)
        pygame.display.update()

except:
    pass

finally:
    saveresults = open(OUTPUT_FILE, 'w')
    for t, r in enumerate(reaction_times):
        saveresults.write(str(t) + ", " + str(r) + "\n")
    saveresults.close()
    pygame.quit()
