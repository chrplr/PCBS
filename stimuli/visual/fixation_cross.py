#! /usr/bin/env python
# Time-stamp: <2022-03-20 13:56:50 christophe@pallier.org>
""" Generates a cross for fixation.
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-128, 127, num=256)
x, y = np.meshgrid(a, a)
cross = 127 * np.logical_or(
    np.logical_and(y == 0, np.logical_and(x > -8, x < 8)),
    np.logical_and(x == 0, np.logical_and(y > -8, y < 8)),
)
plt.imshow(cross, cmap='gray')
plt.show()
