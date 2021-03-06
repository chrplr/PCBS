#! /usr/bin/env python3
# Time-stamp: <2021-03-06 12:06:27 christophe@pallier.org>
""" print multiplication tables

To align the numbers, read about python's format strings
 https://pyformat.info/#number_padding

"""

numbers = range(1, 11)

for num1 in numbers:
    for num2 in numbers:
        print(f'{num1 * num2 :3}', end=' ')
    print()
