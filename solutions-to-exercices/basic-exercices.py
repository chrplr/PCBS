#! /usr/bin/env python3
# Time-stamp: <2021-02-08 11:19:08 christophe@pallier.org>

################################################################################
# prints 1000 times the lines ``All work and no play makes Jack a dull boy.``

for _ in range(1000):
    print("All work and no play makes Jack a dull boy")

################################################################################
# Given a list of numbers, print their product

L = [3, 4, 9, 2]
prod = 1
for term in L:
    prod = prod * term
print(f"Product of terms in {L} = {prod}")

# alternative solution using the numeric module numpy
import numpy as np
np.prod(L)


################################################################################
# Given a list of numbers, print the sum of their square

L = [3, 4, 9, 2]
sum_of_squares = 0
for term in L:
    sum_of_squares = sum_of_squares + (term * term)
print(f"sum of squares of {L} = {sum_of_squares}")

################################################################################
# Given a list of numbers, print the largest one.

L = [3, 4, 9, 2]
maximum = float('-inf')
for term in L:
    if term > maximum:
        maximum = term
print(f"Maximum of {str(L)} = {maximum}")


################################################################################
# Given a list of numbers, print the second largest one.

L = [3, 4, 9, 2]
Ls = sorted(L, reverse=True)  # we sort the list, in descending order
print(f"second maximum of {str(L)} = {Ls[1]}")


