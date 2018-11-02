#! /usr/bin/env python
#! Time-stamp: <2017-09-20 13:21:23 cp983411>


""" 
Implement a simple Reverse Polish Notation Calculator.

Implement a simple Reverse Polish Notation Calculator.
"""

import math

stack = []

def isfloat(string):
    """ check if string can be converted into a float; returns True or False """
    try:
        float(string)
        return True
    except ValueError:
        return False
    

def rpn_eval(expr):
    global stack
    lexpr = expr.split()
    for token in lexpr:
        if isfloat(token):
            stack.append(float(token))
        elif token == 'pi':
            stack.append(math.pi)
        elif token == 'e':
            stack.append(math.e)
        elif token ==  '+':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val1 + val2)
        elif token ==  '-':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 - val1)
        elif token ==  '*':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val1 * val2)
        elif token ==  '/':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val2 / val1)
        elif token == '**':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.append(val1 ** val2)
        elif token == '1/':
            val1 = stack.pop()
            stack.append(1 / val1)
        elif token == 'sum':
            stack = [sum(stack)]
        elif token == 'clr':
            stack = []
        elif token == 'dup':
            val = stack.pop()
            stack.extend([val, val])
        elif token == 'swap':
            val1 = stack.pop()
            val2 = stack.pop()
            stack.extend([val1, val2])
        else:
            print("Unknown command : " + token)


while True:
    expr = input('\nEnter an expression in RPN (or just "Enter" to quit) > ')
    if expr == '':
        break
    rpn_eval(expr)
    for i in stack[::-1]:
        print(i, end='\n')
    
