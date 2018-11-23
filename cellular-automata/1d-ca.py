#! /usr/bin/env python3
# Time-stamp: <2018-11-23 17:56:48 cp983411>

""" An implementation of [Elementay Cellular Automata](https://en.wikipedia.org/wiki/Elementary_cellular_automaton)
"""

import numpy as np
import matplotlib.pyplot as plt


def map(rule, triplet):
    """Applies a CA-rule to a triplet.

    Args:
        rule: list of 8 binary digits representatin a CA-rule
        triplet:  3-uple of bits.

    Returns:
        the result of applying the CA-rule mapping triplets onto {0, 1}

    """
    index = 4 * triplet[0] + 2 * triplet[1] + triplet[2]
    return rule[index]


def get_triplet(boxes, position):
    """Extract the values of boxes at and around position.

    Args:
        boxes: a vector
        position: an index between 1 and len(vector) - 1

    Returns:
         the triplet of values in boxes around position
    """
    return (boxes[position - 1], boxes[position], boxes[position + 1])


def generate(rule, seed, ngenerations):
    """Generates 'ngenerations' applyiong the CA-rule 'rule' to seed.
    """
    nboxes = seed.shape[0]
    pop = np.zeros((ngenerations, nboxes), dtype=int)
    pop[0, :] = seed

    for g in range(1, ngenerations):
        for b in range(1, nboxes - 1):
            pop[g, b] = map(rule, get_triplet(pop[g - 1,:], b))

    return pop


if __name__ == '__main__':
    NBOXES = 100
    NGENERATIONS = 100
    NPATTERNS = 2
    firstgenerations = np.random.randint(2, size=(NPATTERNS, NBOXES))

    for rule in range(256):  # loop over the 256 possible rules
        r = [int(b) for b in f'{rule:08b}']  # convert rule to binary
        for trial in range(NPATTERNS):
            mat = generate(r, firstgenerations[trial], NGENERATIONS)
            plt.imshow(mat)
            plt.savefig(f'r{rule:03d}_{trial}.png')




