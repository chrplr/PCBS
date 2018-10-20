#! /usr/bin/env python
# Time-stamp: <2018-10-18 17:23:31 cp983411>


def print_row(x):
    """ Print all the first non null elements of x"""
    for i in x:
        if i != 0:
            print("%4d" % i, end=' ')
    print('\n', end='')  # go to next line


def next_row(x):
    """ x is a list of integers; return a new list where the ith element is the sum of x[i-1] and x[i] """
    y = [0] * len(x)
    for i in range(1, len(x)):
        y[i] = x[i - 1] + x[i]
    return y


u = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while u[-1] == 0:  # stops when the last column of u is not zero
    u = next_row(u)
    print_row(u)
