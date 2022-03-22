#! /usr/bin/env python
# Time-stamp: <2022-03-20 14:01:25 christophe@pallier.org>
""" Generates a square with white noise
"""

import numpy as np
from numpy.random import rand

import matplotlib.pyplot as plt

M = 127 + 42 * rand(128, 128)

plt.imshow(M, cmap='gray')
plt.show()
plt.imsave('white-noise.png', M, cmap='gray')
