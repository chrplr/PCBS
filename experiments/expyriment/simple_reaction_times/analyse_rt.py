#! /usr/bin/env python
# Time-stamp: <2021-03-25 13:42:24 christophe@pallier.org>

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1], comment='#', na_values='None')

print(data.head())
print(data.describe())

print('Excluding the first 5 trials:')
print(data[5:].describe())


fig = plt.figure()

ax1 = fig.add_subplot(131)
ax1.stem(data.RT)
ax1.title.set_text('RT ~ Trial')

ax2 = fig.add_subplot(132)
ax2.boxplot(data.RT[~np.isnan(data.RT)])
ax2.title.set_text('Distrib. of RT')


ax3 = fig.add_subplot(133)
ax3.scatter(data.wait, data.RT)
ax3.title.set_text('RT ~ Wait time')

plt.show()
