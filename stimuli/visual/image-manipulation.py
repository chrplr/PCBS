#! /usr/bin/env python
# Time-stamp: <2022-03-20 15:20:10 christophe@pallier.org>

import numpy as np
import matplotlib.pyplot as plt

from skimage import data
from skimage.color import rgb2gray

original = data.astronaut()
grayscale = rgb2gray(original)
noisy = 0.5 * grayscale + 0.2 * np.random.randn(grayscale.shape[0], grayscale.shape[1])

fig, axes = plt.subplots(1, 3, figsize=(12, 4))
ax = axes.ravel()
ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(grayscale, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")
ax[2].imshow(noisy, cmap=plt.cm.gray)
ax[2].set_title("Noisy")

fig.tight_layout()
plt.show()

