#! /usr/bin/env python
# Time-stamp: <2019-03-09 13:21:08 christophe@pallier.org>

""" Display a fractal: the [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake).

This a is nice example of the power of [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))

"""

from time import sleep
from turtle import clear, speed, forward, left, right, done
import turtle

l = 300

def koch(n, l):
    if n == 0:
        forward(l)
    else:
        koch(n - 1, l / 3)
        left(60)
        koch(n - 1, l / 3)
        right(120)
        koch(n - 1, l / 3)
        left(60)
        koch(n - 1, l / 3)

koch(3, 400)

turtle.exitonclick()
