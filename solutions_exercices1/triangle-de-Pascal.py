#! /usr/bin/env python
# Time-stamp: <2018-10-18 17:23:31 cp983411>

import numpy as np


##########################
# Three ways of printing
def print_row(u):
    """ prints all first non null elements of u"""
    for e in u:
        if e != 0:
            print(e, end=' ')
        else:
            break
    print('\n', end='')


def print_row2(u):
    for e in u:
        if e != 0:
            print(f"{e:4d}", end=' ')
        else:
            break
    print('\n', end='')


def print_row3(u):
    print(*[e for e in u if e != 0], sep=' ')


##################################################
# 2 versions of generating the Pascal triangle
def version1(N):
    x = [0] * N
    x[0] = 1
    while x[-1] == 0:  # stops when the last column of u is not zero
        print_row(x)
        y = [0] * len(x)
        y[0] = 1
        for i in range(1, len(x)):
            y[i] = x[i - 1] + x[i]
        x = y


def version2(N):  # using numpy arrays
    u = np.zeros(N, dtype='int')
    u[0] = 1

    while u[-1] == 0:
        print_row(u)
        u = np.hstack([0, u[:-1]]) + u


if __name__ == '__main__':
    version1(12)
    version2(12)
