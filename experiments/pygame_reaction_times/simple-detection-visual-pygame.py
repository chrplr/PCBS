#! /usr/bin/env python
# Time-stamp: <2021-03-25 13:26:23 christophe@pallier.org>
""" This is a simple reaction time experiment.

At each trial, a cross is displayed after some random time interval.
The user must click as quickly as possible on a key or a mouse button.

Reaction times are measured and saved in a file for further analyses.

"""

import random
import pygame

N_TRIALS = 20  # total number of trials
MIN_WAIT_TIME = 1000
MAX_WAIT_TIME = 2000
MAX_RESPONSE_DELAY = 2000
RESULT_FILE = 'reaction_times.csv'


def create_window():
    screen = pygame.display.set_mode((1280, 960))
    #screen = pygame.display.set_mode((0, 0),
    #                                  pygame.DOUBLEBUF | pygame.FULLSCREEN)
    pygame.mouse.set_visible(False)
    return screen


def clear_screen(screen):
    screen.fill(pygame.Color('black'))
    pygame.display.flip()


def display_instruction(screen, x, y):
    myfont = pygame.font.SysFont(pygame.font.get_fonts()[0], 32)
    line1 = myfont.render("When you see a cross, press the SPACE BAR as quickly as possible.", 1, pygame.Color('white'))
    line2 = myfont.render("Press it now to start!", 1, pygame.Color('white'))
    screen.blit(line1, (x, y))
    screen.blit(line2, (x, y + 60))
    pygame.display.flip()


def present_cross(x, y, size, color):
    pygame.draw.line(screen, color, (x, y - size), (x, y + size), 4)
    pygame.draw.line(screen, color, (x - size, y), (x + size, y), 4)
    pygame.display.flip()


def wait_for_keypress():
    key_pressed = False
    while not key_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key_pressed = True


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

def save_data(waiting_times, reaction_times, filename=RESULT_FILE):
    with open(filename, 'wt') as f:
        f.write('Wait,RT\n')
        for wt, rt in zip(waiting_times, reaction_times):
            f.write(f"{wt},{rt}\n")


##### main

pygame.init()
screen = create_window()
r = screen.get_rect()
W, H = r.width, r.height
center_x = W // 2
center_y = H // 2

waiting_times = []
reaction_times = []

display_instruction(screen, 20, center_y)
wait_for_keypress()
clear_screen(screen)

pygame.time.delay(1000)

for i_trial in range(N_TRIALS):
    clear_screen(screen)

    waiting_time = random.randint(MIN_WAIT_TIME, MAX_WAIT_TIME)
    pygame.time.delay(waiting_time)

    present_cross(center_x, center_y, 20, pygame.Color('white'))

    reaction_time = measure_reaction_time()
    if reaction_time is None:  # escape pressed
        break

    waiting_times.append(waiting_time)
    reaction_times.append(reaction_time)
    print(i_trial, waiting_time, reaction_time)

save_data(waiting_times, reaction_times)
pygame.quit()
