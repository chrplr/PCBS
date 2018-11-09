

import pandas as pd

a = pd.read_csv('Lexique382/Lexique382.txt', sep='\t')

b = a[['1_ortho', '10_freqlivres']].rename(columns={'1_ortho': 'ortho',
                                                    '10_freqlivres':'freql'})

b.to_csv('ortho-freql.txt', sep='\t', index=False)
