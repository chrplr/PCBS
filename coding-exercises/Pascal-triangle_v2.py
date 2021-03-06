#! /usr/bin/env python
# Time-stamp: <2021-03-06 09:56:09 christophe@pallier.org>
""" Computes and print Pascal's Triangle.

Usage:  pascal_triangle_v2 N

Argument:
   N        an integer >= 1
"""

from docopt import docopt
import numpy as np


def pascal_triangle(nlines):
    row = np.zeros(nlines, dtype='int')
    row[0] = 1
    for _ in range(nlines):
        print(*[f"{e:5}" for e in row if e != 0], sep=' ')
        row = np.hstack([0, row[:-1]]) + row


if __name__ == '__main__':
    args = docopt(__doc__)

    n = int(args['N'])
    pascal_triangle(n)
