#! /usr/bin/Rscript
# Time-stamp: <2021-03-25 13:30:34 christophe@pallier.org>

data = read.csv('reaction_times.csv')
summary(data)

par(mfcol=c(1, 2))
with(data, {
    boxplot(RT)
    plot(RT ~ Wait)
})

cat('\nCheck out the graphics in Rplots*.pdf\n\n')
