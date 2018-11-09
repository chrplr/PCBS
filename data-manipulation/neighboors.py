#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# Time-stamp: <2007-04-25 12:25:58 pallier>
from dico import *

if __name__ == '__main__':
    words = open('liste.txt').read().splitlines()
    mydic = dico()
    mydic.import_words(words)

    wlist =  ['triple','vend','beau','robe']
    wlist.extend(random.sample(words,50))

    # return neighoors_by_substitution:
    for w in wlist:
        print "Voisins par substitution de '%s'" % (w), mydic.neighboors_substitution(w)

    # return neighoors_by_deletion:
    for w in wlist:
        print "Voisins par deletion de '%s'" % (w), mydic.neighboors_deletion(w)

    # return neighoors_by_addition:
    for w in wlist:
        print "Voisins par addition de '%s'" % (w), mydic.neighboors_addition(w)

    # return neighoors_by_transposition:
    for w in wlist:
        print "Voisins par transposition de '%s'" % (w), mydic.neighboors_transposition(w)

