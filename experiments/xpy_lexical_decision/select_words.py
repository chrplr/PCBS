""" extract words from lexique database """

import pandas

lex = pandas.read_csv("http://www.lexique.org/databases/Lexique382/Lexique382.tsv", sep='\t')

subset = lex.loc[(lex.nblettres == 5) & (lex.cgram == "NOM") & (lex.freqfilms2 > 10) & (lex.nombre == 's')]

samp = subset.sample(100)

samp2 = samp.rename(columns = {'ortho':'item'})
samp2.item.to_csv('words.csv', index=False)


