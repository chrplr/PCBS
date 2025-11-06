#! /usr/bin/env python
# Time-stamp: <2022-03-20 15:03:09 christophe@pallier.org>
""" Generates a Bull's eye
"""

import numpy as np
import matplotlib.pyplot as plt


def bullseye():
    a = np.linspace(-128, 127, num=256)
    x, y = np.meshgrid(a, a)
    r = np.sqrt(x * x + y * y)
    red = 128 + 127 * np.logical_or(r < 32, r >= 128)
    green = 128 + 127 * np.logical_or(np.logical_and(r >= 28, r < 80),
                                  r >= 128)
    blue = 128 + 127 * (r >= 72)
    d = np.dstack((red,green, blue))
    return d.astype('uint8')

if __name__ == '__main__':
    a = bullseye()
    print(a)
    plt.imshow(a)
    plt.show()
    plt.imsave('bullseye.png', a)
