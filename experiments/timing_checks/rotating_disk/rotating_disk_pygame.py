#! /usr/bin/env python
import pygame
import sys
import math

pygame.init()

screen = pygame.display.set_mode((1920,1080))
clock = pygame.time.Clock()

prev_t = pygame.time.get_ticks()

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    t = pygame.time.get_ticks()
    print(t, t - prev_t)
    prev_t = t

    screen.fill('Black')
    pygame.draw.circle(screen, 'White', (
        960 + 300 * math.cos(t / 800),
        540 + 300 * math.sin(t / 800)),
        20)

    pygame.display.update()
    clock.tick(60)  # prevents the framerate from exceeding 60 fps

    pygame.time.get_ticks()
