#! /usr/bin/env python
# Time-stamp: <2021-02-08 14:59:15 christophe@pallier.org>

"""
Computing descriptive statistics from a detection experiment

In a signal detection experiment, a faint stimulus (e.g. a faint sound or a faint visual target) is presented or not at each trial and the participant must indicate whether he has perceived it or not. There are four possible outcomes for each trial:

    A hit is when the participant correctly detects the target.
    A miss is when the target was there but the participant did not detect it.
    A false alarm is when the participant reports the presence of the target when it was not actually there.
    A correct rejection is when the participant correctly reports that the target was not present.

One defines;

    The hit rate , equal to #hits / (#hits + #misses)
    The False alarm rate, equal to #false alarms / (#false alarms + # correct rejections)

Let us first suppose that the data from a participant is represented as a string. This string represents a series of trials, each trial being represented by two characters indicating the trial type (1=target present, 0=target absent) and the participant's response (Y=target perceived, N=No target perceived). For example:

---
data = "0Y,0N,1Y,1Y,0N,0N,0Y,1Y,1Y"
---

"""

def hit_fa(data):
    hit, miss, cr, fa = 0, 0, 0, 0
    trials = data.split(',')
    for t in trials:
        if t == '1Y':
            hit += 1
        elif t == '0Y':
            fa += 1
        elif t == '1N':
            miss += 1
        elif t =='0N':
            cr += 1
        else:
            print('Wrong coding:' + t)
    hit_rate = (hit / (hit + miss))
    fa_rate = (fa / (fa + cr))
    return (hit_rate, fa_rate)

################################################################################
print(hit_fa("0Y,0N,1Y,1Y,0N,0N,0Y,1Y,1Y"))


################################################################################
#### Compute hit and fa rates of a series of subjects 

import glob
files = glob.glob('subj*.dat')
for f in files:
    with open(f, 'r') as sub:
        print(f, "%.02f, %.02f" % hit_fa(sub.read()))

################################################################################
#### Graphical Display
scores = []
for f in files:
    with open(f, 'r') as sub:
        scores.append(hit_fa(sub.read()))

import numpy as np
import matplotlib.pyplot as plt

sc = np.array(scores)
plt.scatter(sc[:,1], sc[:,0])
plt.ylim(0, 1)
plt.xlim(0, 1)
plt.show()
