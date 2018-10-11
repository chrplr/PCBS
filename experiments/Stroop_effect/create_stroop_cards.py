#! /usr/bin/env python
# Time-stamp: <2007-06-28 10:23:32 pallier>
# Author: Christophe Pallier (see http://www.pallier.org)

import random
import pygame


def share(list1, list2):
    """ returns True if list1 and list2 have (at least) one identical element in the same position."""
    assert len(list1) == len(list2)
    return len([i for i, j in zip(list1, list2) if i == j]) > 0

def create_stroop_card(items):
    """ items is a dictionary word->color, e.g. {'rouge':'red', 'bleu':'blue', 'vert':'green', 'jaune':'yellow'}
    returns a card with 4 columns and 8 rows as a pygame surface """

    words = list(items.keys())
    colors = list(items.values())

    ncol = 4
    nrow = 8
    W, H = 800, 600
    font = 'Inconsolata.ttf'
    font_size = 44
    font = pygame.font.Font(font, font_size)

    grid = pygame.Surface((W, H))
    label = pygame.Surface((W, H))

    previous_row = [-1, -1, -1, -1]  # colors on the current row
    for irow in range(nrow):
        it = random.sample(range(ncol), ncol)
        col = random.sample(range(ncol), ncol)
        while share(it, col) or share(previous_row, col):
            col = random.sample(range(ncol), ncol)

        previous_row = col  # save the colors

        # fill the current row}
        for icol in range(ncol):
            x = icol * W / ncol + 20
            y = irow * H / nrow
            stringc = words[it[icol]]
            color = colors[col[icol]]
            label.fill((0, 0, 0))
            label.blit(font.render(stringc,
                                   True, pygame.color.Color(color)), (0, 0))
            grid.blit(label, (x, y))
    return grid


def create_cards(items, ncards, template):
    for i in range(ncards):
        grid = create_stroop_card(items)
        pygame.image.save(grid, template % (i))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    create_cards({'rouge': 'red',
                  'blanc': 'white',
                  'vert': 'green',
                  'jaune': 'yellow'},
                 4, "Stroop_French_%02d.png")
    create_cards({'red': 'red',
                  'white': 'white',
                  'green': 'green',
                  'yellow': 'yellow'},
                 4, "Stroop_English_%02d.png")
    create_cards({'gorri': 'red',
                  'zuri': 'white',
                  'berde': 'green',
                  'horri': 'yellow'},
                 4, "Stroop_Basque_%02d.png")

    pygame.quit()
