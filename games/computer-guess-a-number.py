#! /usr/bin/env python3
# Time-stamp: <2019-02-11 09:44:35 christophe@pallier.org>

print "Think about a number between 1 and 100 and I will try to guess it"
my 
min = 1
max = 100

myguess = (max + min) // 2
answer = input('Is it ' + str(myguess) + "? ('y'/'+' if your number is higher/'-' if it is lower)")

while answer != 'y':
    if answer == '+':
        min = myguess
    else:
        max = myguess
    myguess = (max + min) // 2
    answer = input('Is it ' + str(myguess) + '? (y/+/-)')

print 'I am so good!!!'
