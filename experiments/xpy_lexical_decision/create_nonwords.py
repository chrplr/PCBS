""" generates 100 nonwords into the file `pseudowords.csv`
"""

import random
import string

alphabet = string.ascii_lowercase


# version 1
def nonword1(length):
    """ returns a random string of `length` alphabetic characters.  """
    s = ""
    for _ in range(length):
        s = s + random.choice(alphabet)

    return s


# version 2
def nonword2(length):
    """ returns a random string of `length` alphabetic characters.  """
    return "".join(random.choices(alphabet, k=length))


def generate_pseudos(n, length, filename):
    liste = [nonword2(length) for _ in range(n)]
    with open(filename, 'wt', encoding='UTF-8') as f:
        print('item', file=f)
        for pw in liste:
            print(pw, file=f)


generate_pseudos(100, 5, 'pseudowords.csv')
