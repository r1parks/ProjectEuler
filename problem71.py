#!/usr/bin/env python
from fractions import Fraction

if __name__ == '__main__':
    delta = Fraction(1, 1)
    best_n = 0
    for d in xrange(10 ** 6, 2, -1):
        n = (d*3)/7
        diff = Fraction(3, 7) - Fraction(n, d)
        if diff < delta and diff > 0:
            delta = diff
            print "{}".format(n)

