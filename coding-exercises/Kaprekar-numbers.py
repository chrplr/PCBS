#! /usr/bin/env python3
# Time-stamp: <2018-11-02 12:47:03 cp983411>

""" List Kaprekar numbers, i.e., positive numbers n such that n = q+r and n^2 = q*10^m+r, for some m >= 1, q >= 0 and 0 <= r < 10^m, with n != 10^a, a >= 1.  (see http://oeis.org/A006886).
"""


def number_to_symbols(number, base=10):
    """Return the representation of 'number' in base 'base'.
    """ 
    assert number == int(number)  # check that number is an integer
    n = number
    symbols = []
    while n > 0:
        val = n % base
        if val < 9:
            valc =str(val)
        else:
            valc = chr(ord('A') + val - 10)  # map digits > 9 onto [A-Z]
        symbols.append(valc)
        n = n // base
    symbols.reverse()
    return symbols


def form_number(list_of_digits, base=10):
    """ returns the number represented by the digits passed as argument. """
    number = 0
    for digit in list_of_digits:
        c = ord(digit)
        if (c >= ord('0')) and (c <= ord('9')):
            val = c - ord('0')
        else:
            val = 10 + c - ord('A')
        number = number * base + val
    return number


def sums_of_parts(n):
    """ returns the sums obtained by splitting the decimal representation of 'n' in two and adding the resulting numbers """
    digits = number_to_symbols(n) 
    sums = []
    for pos in range(len(digits)):
        left = form_number(digits[:pos])
        right = form_number(digits[pos:])
        sums.append(left + right)
    return sums


def is_kaprekar_number(n):
    if n == 1:
        return True
    # excludes higher powers of 10
    if (str(n)[0] == '1') and all([d == '0' for d in str(n)[1:]]):
        return False
    return n in sums_of_parts(n ** 2)


if __name__ == '__main__':
    print([n for n in range(0, 100000) if is_kaprekar_number(n)])
