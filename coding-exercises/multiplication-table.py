#! /usr/bin/env python3
# Time-stamp: <2021-03-06 09:33:07 christophe@pallier.org>
""" print multiplication tables

To align the numbers, read about format strings
 https://pyformat.info/#number_padding

"""

numbers = range(1, 11)

####################################
# solution1 (one table per number) #
####################################
for num1 in numbers:
    print(f'\nTable of {num1 :3}:')
    for num2 in numbers:
        print(f'{num1 :2} x {num2 :2} = {num1 * num2 :3}')

#############################
# solution 2 (single table) #
#############################
print()
print('   ', end='')
for num1 in numbers:
    print(f'{num1 :3}:', end='')
print(end='\n')

for num1 in numbers:
    print(f'{num1 :2}:', end=' ')
    for num2 in numbers:
        print(f'{num1 * num2 :3}', end=' ')
    print(end='\n')  # skip a line
