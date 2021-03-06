#! /usr/bin/env python3
# Time-stamp: <2021-03-06 10:30:25 christophe@pallier.org>

"""Monte Carlo estimation of PI

See https://academo.org/demos/estimating-pi-monte-carlo/

"""

import random

draws = 1000000

hits = 0
for _ in range(draws):
    x = random.random()  # returns a random number (float) between 0 and 1
    y = random.random()
    if x**2 + y**2 < 1:
        hits += 1

print("Estimate=", 4 * hits/draws)

