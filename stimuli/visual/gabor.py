#! /usr/bin/env python
# Time-stamp: <2022-03-21 08:46:44 christophe@pallier.org>
""" Generates a Gabor pattern.
"""

from numpy import linspace, meshgrid, exp, sin, cos, pi

import matplotlib.pyplot as plt


def gabor(contrast, frequency, tilt, fwhm):
    """Generates a Gabor pattern.

    Parameters
    ----------
    contrast: float
       contrast
    frequency: float
       spatial frequency
    tilt: float
       tilt (in radians)
    fwhm: float
       standard deviation of the spatial Gaussian filter 

    Returns
    -------
    2-d numpy array of shape 256x256 containing the gabor pattern
    """

    a = linspace(-128, 127, num=256)
    x, y = meshgrid(a, a)

    return 127 * (1 + contrast * sin(2 * pi * frequency * (y * sin(tilt) + x * cos(tilt)))) \
               * exp(-(x * x + y * y) / 2 / fwhm / fwhm)


if __name__ == '__main__':
    surface = gabor(contrast=0.25,
                    frequency=1 / 32,
                    tilt=35 * pi / 180,
                    fwhm=24)
    plt.imshow(surface, cmap='gray')
    plt.show()
    plt.imsave('gabor.png', surface, cmap='gray')
