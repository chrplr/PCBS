#! /usr/bin/env python
# Time-stamp: <2022-03-21 08:48:36 christophe@pallier.org>

from numpy import linspace, meshgrid, sin, pi
from numpy.random import rand

import matplotlib.pyplot as plt

c = 0.5
f = 1 / 32

a = linspace(start=-64, stop=63, num=128)
x, y = meshgrid(a, a)

N = 2 * (rand(128, 128) > 0.5) - 1
M = 127 * (1 + N * (0.5 + c * sin(2 * pi * f * x)))

plt.imshow(M, cmap='gray')
plt.show()
plt.imsave('contrastmodulatedgrating.png', M, cmap='gray')
