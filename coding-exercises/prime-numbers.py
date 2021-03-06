#! /usr/bin/env python
# Time-stamp: <2021-03-06 09:36:34 christophe@pallier.org>
"""
List all prime numbers between 1 and 1000.
"""

from math import sqrt


def is_factor(d, n):
    """ True if `d` is a divisor of `n` """
    return n % d == 0


def is_prime(n):
    """Returns `True`` if ``n`` is a prime number, else ``False``.
    """
    assert n > 0
    if n == 1:
        return True
    status = True  # until proven false, assume 'n' is a prime number
    # test all potential divisors
    for i in range(2, int(sqrt(n)) + 1):
        if is_factor(i, n):
            status = False  # a divisor exists, therefore  'n' is not prime
            break  # no need to continue
    return status


if __name__ == "__main__":
    for n in range(1, 1001):
        if is_prime(n):
            print(n, end=' - ')

print()
