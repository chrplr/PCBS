#! /usr/bin/env python
# Time-stamp: <2019-02-24 17:36:52 christophe@pallier.org>

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
