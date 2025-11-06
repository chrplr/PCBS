#! /usr/bin/env python3
# Time-stamp: <2019-03-11 09:43:06 christophe@pallier.org>

""" Implements a [Monte Carlo estimation of PI](https://academo.org/demos/estimating-pi-monte-carlo/) """

from numpy.random import ranf


def estimate_pi_over_4(ndraws):
    return sum([(x**2 + y**2) < 1 for (x, y) in zip(ranf(ndraws), ranf(ndraws))]) / ndraws

if __name__ == '__main__':
    for n in [100, 1000, 10000, 100000, 1000000]:
        print(f'\nsample size {n:7d} :', end='  ')
        estimates = [4 * estimate_pi_over_4(n) for _ in range(10)]
        for e in estimates:
            print(f"{e:.5f}", end=' ')


