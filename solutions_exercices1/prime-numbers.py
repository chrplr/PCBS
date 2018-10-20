#! /usr/bin/env python

"""
list the prime numbers between 1 and 1000.
"""

import math


def is_factor(a, b):
    """ True if a is a divisor of b """
    return b % a == 0


def list_prime_numbers(MAX):
    """ returns the list of primes numbers comprised between 1 and MAX (included) """
    premiers = [1]  # 1 is a prime
    # test each integer one by one 
    for n in range(2, MAX + 1):
        prime = True  # until proven false, we assume it is a prime number
        # test all potential divisors
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_factor(i, n):
                prime = False
                break  # no need to continue
        if prime:
            premiers.append(n)

    return premiers


if __name__ == "__main__":
    MAX = 1000
    print(list_prime_numbers(MAX))
