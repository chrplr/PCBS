#! /usr/bin/env python
# Time-stamp: <2021-03-23 21:36:06 christophe@pallier.org>

import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(sys.argv[1], comment='#')

print(data.groupby('block').describe())

sns.catplot(x='block', y='rt', data=data)
plt.show()
