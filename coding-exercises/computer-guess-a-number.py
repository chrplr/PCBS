#! /usr/bin/env python3
# Time-stamp: <2021-02-08 13:44:45 christophe@pallier.org>

import sys

INSTRUCTIONS = """Hello Human!

Think about a number between 1 and 100 and I will try to guess it.

At each trial, I will display a number, and you will respond by 'y' (yes), '+' (target is higher), '-' (target is lower), or press 'q' to quit. (followed by 'Enter')

"""


print(INSTRUCTIONS)

maxi = 101
mini = 1

myguess = (maxi + mini) // 2
found = False
while not(found):
    answer = input('Is it {} (y/+/-/q)? '.format(myguess))
    if answer == 'y':
        print('Yeah!!!')
        found = True
    elif answer == '+':
        mini = myguess
    elif answer == '-':
        maxi = myguess
    elif answer == 'q':
        found = True
    else:
        print("Please type 'y' (yes), '+' (higher), '-' (lower) or 'q' (quit)")
    myguess = (maxi + mini) // 2
    if myguess == mini:
        print("You are cheating! I quit!")
        sys.exit()

