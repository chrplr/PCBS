#! /usr/bin/env python
# Time-stamp: <2022-03-20 13:34:18 christophe@pallier.org>
"""
create wedge and ring checkboard stimuli as used in fMRI retinotopic experiments
Code translated from Matlab code (Lu & Dosher (2014) _Visual Psychophysics_ (page 40)
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(start=-1024, stop=1024, num=2049)
x, y = np.meshgrid(a, a)

theta = np.arctan2(y, x)
r = np.sqrt(x * x + y * y)
swidth = np.pi / 8
mask1 = 2 * np.round(
    (1 + np.sin(2 * theta *
                (2 * np.pi / swidth))) / 2) - 1  # make wedge pattern
r0 = np.array([64, 96, 144, 208, 288, 400, 528, 672, 832,
               1034])  # radii of different rings
mask2 = r < r0[0]
for i in range(1, len(r0)):
    mask2 = mask2 + (2 *
                     (i % 2) - 1) * np.logical_and(r >= r0[i - 1], r < r0[i])
mask3 = mask1 * mask2

Wmask = (theta > -np.pi / 6) & (theta < np.pi / 6)
Rmask = np.logical_and(r > 64, r <= 144) + np.logical_and(r > 672, r < 1024)

Wedge = Wmask * mask3 * 127 + 128
plt.imshow(Wedge, cmap='gray')
plt.show()
plt.imsave('wedge1.png', Wedge, cmap='gray')

Ring = Rmask * mask3 * 127 + 128
plt.imshow(Ring, cmap='gray')
plt.show()
plt.imsave('ring1.png', Ring, cmap='gray')
