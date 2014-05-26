#!/usr/bin/env python

from fractions import Fraction

def sum_of_digits(n):
    return sum(map(int, str(n)))

def cf_to_rational(cf):
    cf = cf[::-1]
    c = Fraction(cf[0], 1)
    for a in cf[1:]:
        c = Fraction(a) + Fraction(c.denominator, c.numerator)
    return c

if __name__ == '__main__':
    e = [2]
    for i in range(1,40):
        e += [1, 2*i, 1]
    c = cf_to_rational(e[:100])
    print str(c)
    print "numerator sum: {}".format(sum_of_digits(c.numerator))
