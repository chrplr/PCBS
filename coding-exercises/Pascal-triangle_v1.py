#! /usr/bin/env python
# Time-stamp: <2021-03-06 09:48:47 christophe@pallier.org>
""" Print [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
"""

N = 10  # number of lines to print

row = [0] * N
row[0] = 1

for _ in range(N):
    for i in row:
        print(i if i != 0 else '', end=' ')
    print()

    old_row = row

    row = [0] * N
    row[0] = 1
    for i in range(1, N):
        row[i] = old_row[i - 1] + old_row[i]

