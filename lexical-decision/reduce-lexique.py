""" extracts some columns from Lexique382.txt """

import pandas as pd

a = pd.read_csv('Lexique382.txt', sep='\t')

b = a[['1_ortho', '4_cgram', '15_nblettres', '9_freqfilms2']].rename(columns={
    '1_ortho': 'ortho',
    '4_cgram': 'categ',
    '15_nblettres': 'length',
    '9_freqfilms2':'freq'})

b.to_csv('lexique382-reduced.txt', sep='\t', index=False)
