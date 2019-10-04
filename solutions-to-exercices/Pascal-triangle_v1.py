#! /usr/bin/env python
# Time-stamp: <2019-10-04 08:59:38 christophe@pallier.org>

""" Compute and print [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle) """


N = 10  # number of lines to print

def print_row(lst):
    """ prints the first non zero elements of lst """
    for x in lst:
        if x != 0:
            print(f'{x:4d}', end=' ')
        else:
            break
    print('\n', end='')


def print_PascalTriangle(N):
    """ prints the first N rows of Pascal Triangle """

    # creates the first row, as a list containing N zeros
    current_row = [0] * N
    current_row[0] = 1

    for _ in range(N):
        print_row(current_row)
        next_row = [0] * N
        next_row[0] = 1
        for i in range(1, N):
            next_row[i] = current_row[i - 1] + current_row[i]
        current_row = next_row


if __name__ == '__main__':
    print_PascalTriangle(N)
