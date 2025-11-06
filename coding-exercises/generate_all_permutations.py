#! /usr/bin/env python
# Time-stamp: <2021-03-05 13:23:33 christophe@pallier.org>

"""Print all permutations of (1..n).

Usage: generate_all_permutations N

Argument:
   N        an integer >= 1
"""

from docopt import docopt


def generate_all_permutations(seq):
    """ A generator of all the permutations of the sequence 'seq') """
    # Note the use of the ``yield`` operator allowing us to avoid creating a list
    # inside the generator function. Check python's documentation about ``yield``
    if len(seq) == 1:
        yield list(seq)
    else:
        for perm in generate_all_permutations(seq[:-1]):
            for pos in range(len(seq)):
                newperm = perm.copy()
                newperm.insert(pos, seq[-1])
                yield newperm


if __name__ == '__main__':
    args = docopt(__doc__)

    n = int(args['N'])
    for perm in generate_all_permutations(range(1, n + 1)):
        print(' '.join(map(str, perm)))
