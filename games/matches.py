#! /usr/bin/env python3
# Time-stamp: <2019-01-30 19:14:57 cp983411>

# Inspired from the Atom Basic program "Matches" listed
# in *The Acorn Atom Magick Book* (Timedata, 1981)

import random

n_matches = 21 + random.randint(0, 11)

print("""Welcome. Let's play the game of Matches:
We take turns to remove 1, 2 or 3 matches.
The one left with the last match loses.
""")

while n_matches > 0:

    if n_matches > 1:
        print("|" * n_matches)
        print(f"There are {n_matches} matches.")
    else:
        print("There is one match left. I win!")
        break

    resp = input('How many do you take (1-3)? ')
    while not resp in ['1', '2', '3', 'q']:
        resp = input('How many do you take (1-3)? ')

    if resp == 'q':  # Quits the game
        break

    you_take = int(resp)
    n_matches -= you_take

    if n_matches < 2:
        print('I win!')
        break

    r = n_matches % 4
    i_take = (r + 3) % 4
    if r == 1:
        i_take = 1 + random.randint(0, 2)

    n_matches -= i_take
    if n_matches == 0:
        print('You win!')
        break

    print(f'You took {you_take}. I took {i_take}')
