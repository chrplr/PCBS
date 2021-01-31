#!/usr/bin/env python3

# Time-stamp: <2019-12-31 18:00:25 christophe@pallier.org>


""" Solver for the Eight queens problem """

# http://code.activestate.com/recipes/576647-eight-queens-six-lines/

""" As there can be only one queen per column and per row, we can represent a winning solution by a set of 8 numbers, on per line,  which represent the column in which there is a queen. Because the columns must be different, the solutions are a subset of the permutations of 8 numbers. We just have to check that no two queens are in the same diagonal.

The technique for checking the diagonals is to add or subtract the column number from each entry, so any two entries on the same diagonal will have the same value (in other words, the sum or difference is unique for each diagnonal). Now all we have to do is make sure that the diagonals for each of the eight queens are distinct. So, we put them in a set (which eliminates duplicates) and check that the set length is eight (no duplicates were removed).

Any permutation with non-overlapping diagonals is a solution. So, we print it and continue checking other permutations."""


from itertools import permutations


def board(vec):
    '''Translate column positions to an equivalent chess board.

    vec is a list of 8 numbers

    >>> board([0, 4, 7, 5, 2, 6, 1, 3])
    Q-------
    ----Q---
    -------Q
    -----Q--
    --Q-----
    ------Q-
    -Q------
    ---Q----

    '''
    n = len(vec)
    return "\n".join('-' * i + 'Q' + '-' * (n - i - 1) for i in vec)


n = 8
cols = range(n)
solutions = [vec for vec in permutations(cols)
             if n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols))]

for i, vec in enumerate(solutions):
    print(f'###{i + 1:2d}###')
    print(board(vec))
    #print(f"\n=={n}==\n" + board(vec))
