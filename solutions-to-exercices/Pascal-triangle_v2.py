#! /usr/bin/env python
# Time-stamp: <2019-10-04 09:21:37 christophe@pallier.org>


""" Computes and print Pascal's Triangle.

(see <https://en.wikipedia.org/wiki/Pascal%27s_triangle>)
"""

import argparse
import numpy as np


def pascal_triangle(nlines):
    u = np.zeros(nlines, dtype='int')
    u[0] = 1
    for _ in range(nlines):
        print(*[f"{e:5}" for e in u if e != 0], sep=' ')
        u = np.hstack([0, u[:-1]]) + u


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("nlines",
                        type=int,
                        help="number of lines to print") 
    args = parser.parse_args()

    pascal_triangle(args.nlines)
