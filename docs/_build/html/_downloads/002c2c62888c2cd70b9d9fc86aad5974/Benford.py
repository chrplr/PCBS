#! /usr/bin/env python3
# Time-stamp: <2018-11-24 08:41:24 christophe@pallier.org>

""" Check [Benford's law](https://brilliant.org/wiki/benfords-law/) """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


DATAFILE = 'countries.xlsx'  # file containing various demographics data
OUTPUTFILE = 'Benford.pdf'


def open_with_default_app(filepath):
    import subprocess, os, platform
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':    # Windows
        os.startfile(filepath)
    else:                                   # linux variants
        subprocess.call(('xdg-open', filepath))


def left_digit(list_of_numbers):
    """ returns the left most digit from a series of numbers """
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
    data = pd.read_excel(DATAFILE)
    with PdfPages(OUTPUTFILE) as pdf:
        for var in data.columns:
            if np.issubdtype(data[var].dtype, np.number):  # check if the columns is numeric
                numbers = data.loc[~np.isnan(data[var])][var]
                counts = hist(left_digit(numbers))
                counts.plot()
                plt.title(var)
                pdf.savefig()
                plt.gcf().clear()  # clears the plotting area
    open_with_default_app(OUTPUTFILE)
