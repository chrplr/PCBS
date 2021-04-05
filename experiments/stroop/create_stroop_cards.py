#! /usr/bin/env python
# Time-stamp: <2021-04-05 20:26:07 christophe@pallier.org>
# Author: Christophe Pallier (see http://www.pallier.org)

import random
import pygame


def share_item_in_same_position(list1, list2):
    return any([i == j  for (i, j) in zip(list1, list2)])


def create_stroop_card(items, font, background_color=pygame.Color('black')):
    """Create an image representing a Stroop card.

    Argument:
       items              :   a dictionary word->color, e.g. {'rouge':'red', 'bleu':'blue', 'vert':'green', 'jaune':'yellow'}
       font               :   a pygame font object
       background_color 

    Return:
       a pygame surface
    """

    words = list(items.keys())
    colors = list(items.values())
    n = len(items)

    W, H = 800, 600
    margin = 20

    grid = pygame.Surface((W, H))
    grid.fill(background_color)

    label = pygame.Surface((W, H))

    previous_row = [-1, -1, -1, -1]  # colors on the current row
    for i_row in range(n):
        i_word = random.sample(range(n), n)
        i_color = random.sample(range(n), n)
        while share_item_in_same_position(i_word, i_color) or \
              share_item_in_same_position(previous_row, i_color):
            i_color = random.sample(range(n), n)

        previous_row = i_color

        # fill the current row
        y = i_row * H / n + margin

        for i in range(n):
            x = i * W / n + margin
            label.fill(background_color)
            label.blit(font.render(words[i_word[i]],
                                   True, pygame.color.Color(colors[i_color[i]])), (0, 0))
            grid.blit(label, (x, y))
    return grid


def create_cards(items, font, ncards, template):
    for i in range(ncards):
        grid = create_stroop_card(items, font, pygame.Color('black'))
        pygame.image.save(grid, template % (i))


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = './Inconsolata.ttf'
    font_size = 44
    font = pygame.font.Font(font, font_size)

    create_cards({'rouge': 'red',
                  'blanc': 'white',
                  'vert': 'green',
                  'jaune': 'yellow'},
                 font, 4, "Stroop_French_%02d.png")
    create_cards({'red': 'red',
                  'white': 'white',
                  'green': 'green',
                  'yellow': 'yellow'},
                 font, 4, "Stroop_English_%02d.png")
    create_cards({'gorri': 'red',
                  'zuri': 'white',
                  'berde': 'green',
                  'horri': 'yellow'},
                 font, 4, "Stroop_Basque_%02d.png")

    pygame.quit()
