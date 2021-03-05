#! /usr/bin/env python
# Time-stamp: <2021-03-04 16:51:04 christophe@pallier.org>
""" This is a simple reaction time experiment.

At each trial, a cross is displayed after some random time interval.
The user must click as quickly as possible on a key or a mouse button.

Reaction times are measured and saved in a file for further analyses.

"""

import random
import pygame

N_TRIALS = 55  # total number of trials
MAX_RESPONSE_DELAY = 2000
RESULT_FILE = 'reaction_times.csv'


def create_window():
    screen = pygame.display.set_mode((1200, 800), pygame.DOUBLEBUF)
    pygame.mouse.set_visible(False)
    return screen


def present_stimulus(x, y, size, color):
    waiting_time = random.randint(1000, 2000)
    pygame.time.delay(waiting_time)
    pygame.draw.line(screen, color, (x, y - size), (x, y + size), 4)
    pygame.draw.line(screen, color, (x - size, y), (x + size, y), 4)
    pygame.display.flip()
    return waiting_time


def measure_reaction_time(max_response_delay=2000):
    button_pressed = False
    escape = False
    response_delay_elapsed = False
    reaction_time = 0
    pygame.event.clear()  # anticipations will be ignored
    t0 = pygame.time.get_ticks()

    while not button_pressed and not escape and not response_delay_elapsed:
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                escape = True
                break
            if ev.type == pygame.QUIT:
                escape = True
                break
            if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.KEYDOWN:
                reaction_time = pygame.time.get_ticks() - t0
                button_pressed = True

        if pygame.time.get_ticks() - t0 > MAX_RESPONSE_DELAY:
            response_delay_elapsed = True

    if escape:
        return None
    else:
        return reaction_time


##### main

pygame.init()
screen = create_window()
r = screen.get_rect()
W, H = r.width, r.height
center_x = W // 2
center_y = H // 2

waiting_times = []
reaction_times = []
for i_trial in range(N_TRIALS):
    screen.fill(pygame.Color('black'))
    pygame.display.flip()

    waiting_time = present_stimulus(center_x, center_y, 20,
                                    pygame.Color('white'))
    reaction_time = measure_reaction_time()
    if reaction_time is None:  # escape pressed
        break

    waiting_times.append(waiting_time)
    reaction_times.append(reaction_time)
    print(i_trial, waiting_time, reaction_time)

# save the reaction times (except the first five, considered as training)
with open(RESULT_FILE, 'w') as f:
    f.write('Wait,RT\n')
    for wt, rt in zip(waiting_times[5:], reaction_times[5:]):
        f.write(f"{wt},{rt}\n")

pygame.quit()
