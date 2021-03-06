#! /usr/bin/env python
# Time-stamp: <2021-03-06 09:34:39 christophe@pallier.org>
"""
Two taxi companies have differents pricing schemes:

- A charges 4.80€ plus 1.00€/km
- B charges 3.20€ plus 1.20€/km

Finds which company is the cheapest as a function of the distance to travel.
"""

for distance in range(1, 20):
    cost_A = 4.8 + 1.00 * distance
    cost_B = 3.2 + 1.20 * distance
    if cost_A < cost_B:
        best = 'A'
    elif cost_A > cost_B:
        best = 'B'
    else:
        best = 'A or B'

    print(f"{distance :2} km -> {best}")
