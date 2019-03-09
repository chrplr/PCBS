#! /usr/bin/env python
# Time-stamp: <2019-02-08 07:11:38 christophe@pallier.org>

import numpy as np

data = [4, 5, 4, 6, 4, 4, 5, 4]

nloops = 100

means = [np.random.choice(data, size=len(data), replace=True).mean() for _ in range(nloops)]


print(np.mean(means), np.std(means))
