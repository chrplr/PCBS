#! /usr/bin/env python
# Time-stamp: <2018-10-20 13:48:41 cp983411>

"""
    Interpreter of the RodRego register machine.
"""

program = """
deb 2 2 3
inc 1 1
end
"""


DEBUG = True
 
prg = [l.split() for l in program.splitlines()]
registers = [0] * 11

registers[0] = 5
registers[1] = 4

IP = 1  # instruction pointer
while True:
    assert IP < len(prg)

    if DEBUG:
        print('IP = ' + str(IP))
        print(prg[IP])
        print(registers)

    instruc = prg[IP][0]

    if instruc == 'end':
        break

    reg = int(prg[IP][1]) - 1

    if instruc == 'inc':
        registers[reg] += 1
        IP = int(prg[IP][2])

    elif instruc == 'deb':
        if registers[reg] > 0:
            registers[reg] -= 1
            IP = int(prg[IP][2])
        else:
            IP = int(prg[IP][3])
    else:
        print('unknown command: ' + instruc + ' on line ' + str(IP + 1))
        break
