#! /usr/bin/env python
# Time-stamp: <2021-02-09 21:30:08 christophe@pallier.org>

"""Interpreter for RodRego (see http://sites.tufts.edu/rodrego/).

RodRego is a simple register machine simulator illustrating the computational
capabilities of the INC/DEB language model. By inputting different commands,
you can increment and decrement the ten registers (or boxes) to simulate
different computations.

There are three different commands available: INC, DEB, and END

- You can use INC to increment a particular register by one. The syntax for the
INC command is::

    [step] INC [register] [go to step]

- You can use DEB to decrement a particular register by one. The syntax for the DEB command is::

    [step] DEB [register] [go to step] [go to step if already empty]

- Finally, you can use the END command to end a script from running.


An example script might look like:

1 INC 2 2    # Increment 2nd register and go to step (line) 2
2 DEB 3 2 3  # Decrement 3rd register and repeat (got to step 2) until empty (goto to step 3)
3 END        # End program


For more information about RodRego and register machines, read "Secrets of
Computer Power Revealed” on  http://sites.tufts.edu/rodrego/
"""

import sys

def run(program, registers = [0]* 10):
    """Run a Rodrego program.

    Args:
       program: multiline string (one line per instruction)
       registers: list of 10 integer values, initial state of the machine
    """

    #### parser (barebones)
    prog = dict()   # associate steps to instructions
    for line in program.splitlines():
        cleanline = line.strip()  # delete trailing whitespaces
        if cleanline == "":  # skip empty lines
            continue
        if cleanline[0] == "#":  # skip comment lines
            continue
        tokens = cleanline.split()
        if len(tokens) >= 2:  # skip empty lines
            step, code = tokens[0], tokens[1:]
            prog[step] = code
            try:
                firststep
            except NameError:
                firststep = step  # memorize the step associated to the first line of code

    ## interpreter
    IP = firststep  # instruction pointer
    while True:
        print(f'IP -> {IP} {" ".join(prog[IP]):12} {registers}')

        instruction = prog[IP][0].upper()
        if instruction == 'END':
            break

        reg = int(prog[IP][1]) - 1

        if instruction == 'INC':
            registers[reg] += 1
            IP = prog[IP][2]
        elif instruction == 'DEB':
            if registers[reg] > 0:
                registers[reg] -= 1
                IP = prog[IP][2]
            else:
                IP = prog[IP][3]
        else:
            print('Unknown command: ' + instruc + ' on line ' + str(IP + 1))
            break


def test():
    registers = [0] * 10

    # initial state
    registers[0] = 5
    registers[1] = 4

    adder = """
            1 DEB 2 2 3
            2 INC 1 1
            3 END
            """ 

    run(adder, registers)


if __name__ == '__main__':
    # take the name of a file containing a Rodrego program as argument,
    # and execute it
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]}  program r1 r2 r3 r4 r5 r6 r7 r8 r9 r10")
        print("\nInterprets 'program', a text file containing Rodrego code, with the register values r1 to r10 (see http://sites.tufts.edu/rodrego/)")
        sys.exit()

    with open(sys.argv[1], 'r') as f:
        code = f.read()
        registers = [int(i) for i in sys.argv[2:]]
        run(code, registers)


