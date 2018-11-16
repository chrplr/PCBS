#! /usr/bin/env python3
# Time-stamp: <2018-11-16 10:48:27 cp983411>

import pandas as pd

lex = pd.read_csv("lexique382-reduced.txt", sep='\t')

lex.head()

noms = lex.loc[lex.categ == 'NOM']
len(noms)
noms.sample(10)

verbs = lex.loc[lex.categ == 'VERB']
len(verbs)
verbs.sample(10)

hifreq = lex.loc[lex.freq > 50.0]
len(hifreq)
hifreq.sample(10)

lowfreq = lex.loc[(lex.freq < 10.0) & (lex.freq > 1.0)]
len(lowfreq)
lowfreq.sample(10)

