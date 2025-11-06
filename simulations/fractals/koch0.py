#! /usr/bin/env python
# Time-stamp: <2021-02-08 12:40:05 christophe@pallier.org>

""" Displays a fractal: the [Koch snowflake](https://en.wikipedia.org/wiki/Koch_snowflake).

This a is nice example of the power of [recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science))

"""

import turtle


def Koch(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        Koch(n - 1, l / 3)

        turtle.left(60)
        Koch(n - 1, l / 3)

        turtle.right(120)
        Koch(n - 1, l / 3)

        turtle.left(60)
        Koch(n - 1, l / 3)


turtle.penup()
turtle.backward(600)
turtle.pendown()

Koch(1, 400)

Koch(2, 400)

Koch(3, 400)

turtle.exitonclick()
