#! /usr/bin/env python
# Time-stamp: <2021-02-08 13:23:46 christophe@pallier.org>

"""
List prime numbers between 1 and 1000.
"""

import math

def is_factor(a, b):
    """ True if a is a divisor of b """
    return b % a == 0


def is_prime(x):
    """Returns 'True' if 'x' is a prime number, else 'False'.
    """
    assert isinstance(x, int)
    assert x > 0
    if x == 1:
        return True
    status = True  # until proven false, we assume 'x' is a prime number
    # test all potential divisors
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_factor(i, x):
            status = False  # we found a divisor
            break  # no need to continue
    return status


if __name__ == "__main__":
    print([x for x in range(1, 1001) if is_prime(x)])
