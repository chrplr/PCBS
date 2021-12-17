#! /usr/bin/env python3
# Time-stamp: <2021-12-14 15:41:16 christophe@pallier.org>

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def frequency_table(items):
    """ Tabulate the frequencies of occurrence of items in a list.

        Args:
            items: a list of immutable objects (stings, number, ...).

        Returns:
            A pandas.Series mapping the items types to their number
            of occurrences, frequency sorted by their rank
    """
    table = pd.Series()
    for it in items:
        if str(it) in table.index:
            table[str(it)] += 1
        else:
            table[str(it)] = 1
    return table.sort_values(ascending=False)


def frequency_spectrum(ftable):
    """ Computes the frequency spectrum, that is the number of words types in a given frequency class.

    Args:
        ftable: a frequency table associating words (types) to word counts

    Returns:
        a pd.DataFrame mapping words count to number of word types.

    """
    fs = frequency_table(ftable)
    fdf = fs.reset_index().rename(columns = {'index': 'counts', 0: 'ntypes'})  # extract index and transform the pd.Series into a pd.DataFrame
    fdf.counts = fdf.counts.astype('int')
    fdf.sort_values(by=['counts'], inplace=True)
    return fdf


def zipf_plot(ftable, logx=False, logy=False):
    """ Produces Zipf plot from a frequency table (items' rank on the x axis, frequency on the y axis) 

    Args:
        ftable: pd.Series mapping words to their frequencies
    """

    x = 1 + np.arange(len(ftable))
    y = ftable
    if logx:
        x = np.log10(x)
    if logy:
        y = np.log10(y)

    plt.bar(x, y)

    if not logx:
        plt.xticks(x, ftable.index)


if __name__ == '__main__':
    liste = ['a', 'b', 'a', 'c', 'd', 'b', 'e', 'f', 'a', 'a', 'a']
    print(liste)

    a = frequency_table(liste)
    print('Frequency table:')
    print(a)

    zipf_plot(a)
    plt.show()

    b = frequency_spectrum(a)
    print('Frequency spectrum:')
    print(b)

    plt.plot(b.counts, b.ntypes, '-o')
    plt.title('Frequency spectrum')
    plt.show()

