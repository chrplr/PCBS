#! /usr/bin/env python3
# Time-stamp: <2018-11-04 10:40:58 cp983411>

""" print the multiplication tables """

MAX = 10

# display 1
for i in range(1, MAX + 1):
    print(end='\n')  # skip a line
    for j in range(1, MAX + 1):
        print(f'{i:2} x {j:2} = {i*j:2}')


# display 2
print()
print('   ', end='')
for i in range(1, MAX + 1):
    print(f'{i:3}:', end='')
print(end='\n')

for i in range(1, MAX + 1):
    print(f'{i:2}:', end=' ')
    for j in range(1, MAX + 1):
        print(f'{i*j:3}', end=' ')
    print(end='\n')  # skip a line




