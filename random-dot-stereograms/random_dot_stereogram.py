# /usr/bin/env python
# Time-stamp: <2019-02-07 07:44:44 christophe@pallier.org>

""" A random-dot stereogram is stereo pair of images of random dots which when viewed with the eyes focused on a point in front of or behind the images, produces a sensation of depth. This module provides a function that generates such stereograms.

See <https://en.wikipedia.org/wiki/Random_dot_stereogram>.
"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from PIL import Image

def stereogram(imgsize=(80, 80), inner_size=(30, 30), shift=6, gap=20):
    """ Returns a pair of images  a random-dot stereogram. """
    rightimg = numpy.random.binomial(1, p=0.5, size=imgsize)
    leftimg = rightimg
    inner = numpy.random.binomial(1, p=0.5, size=inner_size)

    x, y = (imgsize[0] - inner_size[0]) // 2, (imgsize[1] - inner_size[1]) // 2
    xright = x - shift // 2
    xleft = xright + shift
    rightimg[xright:xright+inner_size[0], y:y+inner_size[1]] = inner
    leftimg[xleft:xleft+inner_size[0], y:y+inner_size[1]] = inner
    return (leftimg, rightimg)


def show_two_images(leftimg, rightimg, gap=10):
    #import matplotlib.pyplot as plt
    img = np.concatenate([leftimg, np.ones((gap, leftimg.shape[1])), rightimg], axis=0)
    plt.imshow(img.transpose(), cmap='gray')
    plt.axis('off')
    plt.show()


def save_stereogram(fname, leftimg, rightimg, gap=10):
    # TODO: not working !!!
    #from PIL import image
    arr = np.concatenate([leftimg, np.ones((gap, leftimg.shape[1])), rightimg], axis=0)
    img = Image.fromarray(arr)
    img_rgb = img.convert('RGB')
    img_rgb.save(fname)


if __name__ == '__main__':
    leftimg, rightimg = stereogram()
    show_two_images(leftimg, rightimg)
    save_stereogram('stereogram.png', leftimg, rightimg)


