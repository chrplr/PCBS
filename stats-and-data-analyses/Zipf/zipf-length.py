#! /usr/bin/env python
# Time-stamp: <2021-12-14 09:48:36 christophe@pallier.org>

""" plot the relationship between word length and frequency """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sas

lex = pd.read_csv('lexique382-reduced.txt', sep='\t')

print(lex.head())

sas.jointplot(lex.length, lex.freq)
plt.show()

lex.logfreq = np.log10(lex.freq + 0.001)
sas.jointplot(lex.length, lex.logfreq)
plt.show()
