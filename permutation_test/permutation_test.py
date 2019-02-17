#! /usr/bin/env python
# Time-stamp: <2019-02-07 11:22:21 christophe@pallier.org>


""" Demonstration of the permutation test to compare two samples (see <https://en.wikipedia.org/wiki/Resampling_(statistics)#Permutation_tests>) """

import numpy as np

set1 = np.array([168, 174, 175, 176])
set2 = np.array([165, 170, 168, 157])

diff = set1.mean() - set2.mean()
print(f"Observed difference between set1 and set2 = {diff:.2f}")


# approach 1: splitting the (permuted) data array
data = np.concatenate((set1, set2))
n1 = len(set1)

# %% time  under ipython
npermutations = 10000
means_H0 = np.empty(npermutations)
pdata = data.copy()
for i in np.arange(npermutations):
    np.random.shuffle(pdata)
    means_H0[i] = pdata[:n1].mean() - pdata[n1:].mean()
# proportion
print(f"Proportions of means above the observed mean under H0:  p-value = {np.mean(means_H0 > diff)}")


# approach 2: using boolean indexing to select two subsets from  data  
data = np.concatenate((set1, set2))
labels = [True] * len(set1) + [False] * len(set2)

# distribution of differences under H0 (random permutations of labels)
npermutations = 10000
means_H0 = np.empty(npermutations)
for i in np.arange(npermutations):
    l = np.random.permutation(labels)
    means_H0[i] = data[l].mean() - data[np.logical_not(l)].mean()

# proportion
print(f"Proportions of means above the observed mean under H0:  p-value = {np.mean(means_H0 > diff)}")



# graphics
import matplotlib.pyplot as plt

plt.hist(means_H0)
plt.plot([diff,  diff], [-1, 500], color='red', linestyle='-', linewidth=2)
plt.show()


# advanced syntax
def randomdiff(data, n):
    np.random.shuffle(data)
    return data[:n].mean() - data[n:].mean()

pdata = data.copy()
means_H0 = [randomdiff(pdata, n1) for _ in np.arange(npermutations)]
print(f"Proportions of means above the observed mean under H0:  p-value = {np.mean(means_H0 > diff)}")

