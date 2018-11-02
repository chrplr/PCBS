#! /usr/bin/env python
# Time-stamp: <2018-10-20 13:32:29 cp983411>


STRING = 'Cogmaster'
FILENAME = 'aga.txt'

f = open(FILENAME, 'r', encoding='utf-8')
for line in f:
    if STRING in line:
        print(line, end='')
