#! /usr/bin/env python

""" Estimate the statistical power of Student t test. """

import matplotlib.pyplot as plt
import numpy as np
import numpy.random
import scipy.stats as stats

def compute_p_value(effect_size, samples_size):
    """ generates two normally distributed random samples of size `n`,
    from two population differing in means by `effect_size`.

    Returns:the p-value associated to the (two-tail) Student T-test comparing the two samples.
    """
    group_1 = np.random.randn(samples_size)
    group_2 = effect_size + np.random.randn(samples_size)
    _, p_val = stats.ttest_ind(group_1, group_2)
    return p_val


def power(nsimulations, alpha_level, effect_size, samples_size):
    """ returns the probability to detect an effect by running 'nsimulations' t-tests. """
    detections = [compute_p_value(effect_size, samples_size) <= alpha_level
                  for _ in range(nsimulations)]
    return sum(detections)/len(detections)


if __name__ == '__main__':

    alpha = 0.05
    effect_size = 0.5
    n_simulations = 1000
    samples_sizes = [5, 8, 10, 16, 20, 30, 40, 50, 100, 200]

    powers = [100 * power(n_simulations, alpha, effect_size, n)
              for n in samples_sizes]

    plt.plot(samples_sizes, powers)
    plt.title(f'Power of T-test (effect={effect_size})')
    plt.xlabel('Sample size')
    plt.ylabel('Power (%)')
    plt.grid()
    plt.show()
