#! /usr/bin/env python3
# Time-stamp: <2021-03-06 12:20:14 christophe@pallier.org>

""" Implements a [Monte Carlo estimation of PI](https://academo.org/demos/estimating-pi-monte-carlo/) """

import numpy as np
from numpy.random import default_rng

N = 10000000

rng = default_rng()
x = rng.uniform(low=0.0, high=1.0, size=N)
y = rng.uniform(low=0.0, high=1.0, size=N)

print("est =", 4 * np.mean(x**2 + y**2 < 1))
