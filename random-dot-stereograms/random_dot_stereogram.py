# /usr/bin/env python
# Time-stamp: <2021-02-26 12:49:34 christophe@pallier.org>

""" Display a random dot stereogram.

A random-dot stereogram is stereo pair of images of random dots which when
viewed with the eyes focused on a point in front of or behind the images,
produces a sensation of depth. This module provides a function that generates
such a stereogram (Ref: <https://en.wikipedia.org/wiki/Random_dot_stereogram>)

"""

import numpy as np
import numpy.random
import matplotlib.pyplot as plt

def stereogram(imgsize=(80, 80), inner_size=(30, 30), shift=6):
    """ Returns a pair of images (numpy 2-arrays)forming  a random-dot stereogram. """

    background = numpy.random.binomial(1, p=0.5, size=imgsize)
    foreground = numpy.random.binomial(1, p=0.5, size=inner_size)

    #  top left position of the foreground before shifting
    x = (imgsize[0] - inner_size[0]) // 2
    y = (imgsize[1] - inner_size[1]) // 2

    rightimg = background
    xright = x - shift // 2
    rightimg[xright:(xright + inner_size[0]), y:(y + inner_size[1])] = foreground

    leftimg = background
    xleft = xright + shift
    leftimg[xleft:(xleft + inner_size[0]), y:(y+inner_size[1])] = foreground

    return (leftimg, rightimg)


def show_two_images(leftimg, rightimg, gap=10):
    """ displays two images side by side, separated by a white ``gap``  """
    img = np.concatenate([leftimg, np.ones((gap, leftimg.shape[1])), rightimg], axis=0)
    plt.imshow(img.transpose(), cmap='gray')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    leftimg, rightimg = stereogram()
    show_two_images(leftimg, rightimg)


