#! /usr/bin/env python
# Time-stamp: <2021-04-15 10:23:31 christophe@pallier.org>
# Author: Christophe Pallier (see http://www.pallier.org)

import random
import pygame

RED = pygame.Color('red')
YELLOW = pygame.Color('yellow')
GREEN = pygame.Color('green')
WHITE = pygame.Color('white')
BLACK = pygame.Color("black")


french = (('rouge', RED), ('blanc', WHITE), ('jaune', YELLOW), ('vert', GREEN))
english = (('red', RED), ('white', WHITE), ('yellow', YELLOW), ('green', GREEN))
basque = (('gorri', RED), ('zuri', WHITE), ('horri', YELLOW), ('berde', GREEN))


def match(word, color, items):
    return (word, color) in items


def generate_array(n_row, n_col, items):
    """ returns an array (list of lists) of n rows, p columns
        containing pairs (word, color)
        such that there is no repetition of color on line,
        nor in successive rows.
    """
    words = [x for x, y in items]
    colors = [y for x, y in items]
    array = []

    # we fill row by row, checking compatibility with previous row
    previous_row = [""] * n_col  # colors on the current row
    for i_row in range(n_row):
        perm1 = random.sample(words, n_col)
        perm2 = random.sample(colors, n_col)
        while any([match(word, color, items) for word, color in zip(perm1, perm2)]) or \
              any([col1 == col2 for col1, col2 in zip(previous_row, perm2)]):
            perm2 = random.sample(colors, n_col)

        array.append(list(zip(perm1, perm2)))
        previous_row = perm2

    return array


def create_stroop_card(array, font, background_color=pygame.Color('black')):
    """Create an image representing a Stroop card.

    Argument:
       items              :   a table (list of lists) of pairs (string, color)
       font               :   a pygame font object
       background_color 

    Return:
       a pygame surface
    """

    W, H = 800, 600
    margin = 20
    grid = pygame.Surface((W, H))
    grid.fill(background_color)

    n_row = len(array)
    n_col = len(array[0])
    for i_row, row in enumerate(array):
        for i_col, pair in enumerate(row):
            word, color = pair
            grid.blit(font.render(word, True, color),
                      (i_col * W / n_col + margin, i_row * H / n_row + margin))
    return grid


def create_cards(items, font, ncards, template):
    for i in range(1, ncards + 1):
        word_color_array = generate_array(4, 4, items)
        grid = create_stroop_card(word_color_array, font, pygame.Color('black'))
        pygame.image.save(grid, template % i)


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = './Inconsolata.ttf'
    font_size = 44
    font = pygame.font.Font(font, font_size)

    create_cards(french, font, 4, "Stroop_French_%02d.png")
    create_cards(english, font, 4, "Stroop_English_%02d.png")
    create_cards(basque, font, 4, "Stroop_Basque_%02d.png")

    pygame.quit()
