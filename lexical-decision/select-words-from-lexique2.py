#! /usr/bin/env python3
# Time-stamp: <2018-11-16 10:48:27 cp983411>

import pandas as pd

lex = pd.read_csv("lexique382-reduced.txt", sep='\t')

lex.head()

subset = lex.loc[(lex.length >= 5) & (lex.length <=8)]

noms = subset.loc[subset.categ == 'NOM']
verbs = subset.loc[subset.categ == 'VER']

noms_hi = noms.loc[noms.freq > 50.0]
noms_low = noms.loc[(noms.freq < 10.0) & (noms.freq > 1.0)]

verbs_hi = verbs.loc[verbs.freq > 50.0]
verbs_low = verbs.loc[(verbs.freq < 10.0) & (verbs.freq > 1.0)]

N = 20

noms_hi.sample(N).ortho.to_csv('nomhi.txt', index=False)
noms_low.sample(N).ortho.to_csv('nomlo.txt', index=False)
verbs_hi.sample(N).ortho.to_csv('verhi.txt', index=False)
verbs_hi.sample(N).ortho.to_csv('verlo.txt', index=False)



