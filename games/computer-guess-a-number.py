#! /usr/bin/env python3
# Time-stamp: <2019-03-09 12:25:00 christophe@pallier.org>

""" Little interactive game where the computer tries to guess a number between 1 and 100 that you have in mind  """

print("Think about a number between 1 and 100 and I will try to guess it")
min = 1
max = 100

myguess = (max + min) // 2
answer = input('Is it ' + str(myguess) + "?   (Press '+' if your number is higher, '-' if it is lower, 'y' if I am correct then 'Return')")

while answer != 'y':
    if answer == '+':
        min = myguess
    else:
        max = myguess
    myguess = (max + min) // 2  # dichotomous search
    answer = input('Is it ' + str(myguess) + '? (y/+/-)')

print('I am so good!!!')
