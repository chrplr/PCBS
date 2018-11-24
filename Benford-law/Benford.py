#! /usr/bin/env python3
# Time-stamp: <2018-11-24 08:41:24 cp983411>

""" Check [Benford's law](https://brilliant.org/wiki/benfords-law/) """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


def left_digit(list_of_numbers):
    return [int(f'{np.abs(n):e}'[0])
            for n in list_of_numbers if float(n) != 0.0]


def hist(list_of_digits):
    counts = {}
    for d in range(1, 10):
        counts[d] = 0
    for d in list_of_digits:
        counts[d] += 1
    return pd.Series(counts)


if __name__ == '__main__':
    data = pd.read_excel('countries of the world.xlsx')
    with PdfPages('Benford.pdf') as pdf:
        for var in data.columns:
            if np.issubdtype(data[var].dtype, np.number):  # check if the columns is numeric
                numbers = data.loc[~np.isnan(data[var])][var]
                counts = hist(left_digit(numbers))
                counts.plot()
                plt.title(var)
                pdf.savefig()
                plt.gcf().clear()  # clears the plotting area
