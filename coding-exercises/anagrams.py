#! /usr/bin/env python3
# Time-stamp: <2021-02-08 11:43:58 christophe@pallier.org>
# License: GPL-2

"""
Input: a list with *one* word per line on the standard input

Output: all anagrams on the standard output 
"""

import sys

input_words = sys.stdin.readlines()  # read the whole standard input

##########################################################
# associate each word to a key consisting of its sorted letters
anagrams = {}
for word in input_words:
    word = word.strip()  # delete trailing whitespaces
    key = "".join(sorted(word))  # compute key
    if key in anagrams.keys():
        if word not in anagrams[key]:
            anagrams[key].append(word)
    else:
        anagrams[key] = [word]

# delete single word entries
single_entries = [k for k, lw in anagrams.items() if  len(lw) == 1]
for k in single_entries:
    del(anagrams[k])

#####################
# prints the anagrams
liste = []
for k, lw in anagrams.items():
    liste.append(" ".join(sorted(lw)))

liste.sort()

for w in set(liste):
     print(w)


