#! /usr/bin/env python
# Time-stamp: <2018-11-23 11:23:25 cp983411>

""" plot the relationship between word length and frequency """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sas

lex = pd.read_csv('../lexical-decision/lexique382-reduced.txt', sep='\t')

print(lex.head())

sas.jointplot(lex.length, lex.freq)
plt.show()

lex.logfreq = np.log10(lex.freq + 0.001)
sas.jointplot(lex.length, lex.logfreq)
plt.show()
