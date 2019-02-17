#! /usr/bin/env python3
# Time-stamp: <2019-01-30 19:14:57 cp983411>

# Inspired from the Atom Basic program "Hammurabi" listed
# in *The Acorn Atom Magick Book* (Timedata, 1981)

import random

h, s, a = 100, 3000, 1000

year = 0

while h > 0:
    print("O Hammurabi, king of Sumaria,")
    print(f"Your subjects now number {h}.")
    print(f"Your kingdom covers {a} acres.")
    print(f"You have {s} bushels of grain.")

    l = random.randint(20, 25)
    print(f"Land is {l} bushels per acre")
    print('')

    e = input("How many acres do you buy? ")
    e = int(e)
    assert e * l <= s
    if e == 0:
        e = input("How many acres do you sell? ")
        e = int(e)
        e = -e

    a = a + e
    s = s - (l * e)
    print(f"{s} bushels remaining.")
    f = input("How many bushels for food? ")
    f = int(f)
    assert(f <= s )

    s = s - f
    print(f"{s} bushels remaining.")

    p = input("How many bushels for seed? ")
    p = int(p)
    assert (p <= s)

    s = s - p
    print(f"{s} bushels remaining.")

    if p > 2 * a:  # max production because of acres
        p = 2 * a

    if p > 25 * h:  # max produciton because of human
        p = 25 * h  

    r = random.randint(0, 1 + s // 2)  # rats
    c = p // 4 + random.randint(0, p * 4)
    s = s + c - r

    # update population
    d = h - f // 15 
    if d < 1:
        d = 0

    h = h - d
    n = h // 20 + random.randint(0, h // 20) # newborn
    h = h + n

    z  = 0  # death by pleague
    if random.randint(1, 4) == 1:
        z = h // 3 + random.randint(0, h // 4)
    h = h - z

    year = year + 1
    print("O King, I beg to report that")
    print("in Year {year} of your reign,")
    print("you harvested {c} bushels")
    if r > 0:
        print(f"But rats ate {r} bushels.")
    print(f"{d} People starved, {n} were born.")
    if z > 0:
        print(f"{z} dies of pleague")

print("As you have no subjects left,")
print("This is the end of your reign.")
