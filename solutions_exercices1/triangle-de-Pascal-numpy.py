#! /usr/bin/env python

""" Displays Pascal triangle """

import numpy as np

N = 12
u = np.zeros(N, dtype='int')
u[0] = 1

while u[-1] == 0:
    print(u
    u = np.hstack([0, u[:-1]]) + u
