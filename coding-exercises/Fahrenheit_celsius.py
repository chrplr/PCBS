#! /usr/bin/env python3
"""
Temperature unit converter.

@author: christophe@pallier.org
"""

import sys

def F_to_C(f):
    """Conversion °F -> °C

    Args:
        f (float): temperature in °F

    Returns:
        float: temperature in °C
    """
    return (f - 32) * 5 / 9


def C_to_F(c):
    """Conversion °C -> °F

    Args:
        c (float): temperature in °C

    Returns:
        float: temperature in °F
    """

    return (c * 9 / 5) + 32


def str2temp(string):
    """Converts a string into a temperature (value, unit).

    Args:
        string (str): string representation of a temperature

    Returns:
        a couple (float, char) where float is the temperature value and char is 'C' or 'F'
    """
    string = string.strip() # remove trailing whitespaces
    value = string[:-1]  # get the first characters but last
    try:
       val = float(value)
    except ValueError:
        try:
            val = float(string[:-2])  # maybe there is a '°' before the unit
        except ValueError:
            raise ValueError("The first n-1 characters of %s are not a float" % string)

    unit = string[-1].upper()  # get the last character
    if unit not in "CF":
        raise ValueError("unknown unit %s should end in C or F" % string)
    return (val, unit)



def help():
    print('Usage: %s', sys.argv[0])
    print('Convert a list of temperatures from Celsius to Farenheit or vice-versa.')
    print('Each line on the standard input should contain one temperature of the form xxx{F|C} ')
    print('Entering an empty line stops the program')



if __name__ == '__main__':
    if len(sys.argv) > 1:
        help()
        sys.exit()

    for line in sys.stdin:
        if line.strip() == "":
            break
        value, unit = str2temp(line)
        if unit == 'C':
            print("%.1f°C = %.1f°F" % (value, C_to_F(value)))
        elif unit == 'F':
            print("%.1f°F = %.1f°C" % (value, F_to_C(value)))
        else:
            print("Unknown unit : %s (should be 'C' or 'F')" % unit)


