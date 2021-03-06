#! /usr/bin/env python3
# Time-stamp: <2021-03-06 12:32:33 christophe@pallier.org>
"""Monte Carlo estimation of PI

See https://academo.org/demos/estimating-pi-monte-carlo/

"""

import timeit

###########################
# solution 1. Basic Python

import random

draws = 1000000

starttime = timeit.default_timer()

hits = 0
for _ in range(draws):
    x = random.random()  # returns a random number (float) between 0 and 1
    y = random.random()
    if x**2 + y**2 < 1:
        hits += 1

estimate1 = 4 * hits / draws

exec_time1 = timeit.default_timer() - starttime

print(" Estimate =", estimate1, " time of execution =", exec_time1)

###############################################
# solution 2. Using Numpy <https://numpy.org/>

import numpy as np
from numpy.random import default_rng

rng = default_rng()

draws = 1000000

starttime = timeit.default_timer()

x = rng.uniform(low=0.0, high=1.0, size=draws)
y = rng.uniform(low=0.0, high=1.0, size=draws)
estimate2 = 4 * np.mean(x**2 + y**2 < 1)

exec_time2 = timeit.default_timer() - starttime

print(" Estimate =", estimate2, " time of execution =", exec_time2)
