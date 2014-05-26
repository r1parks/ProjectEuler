#!/usr/bin/env python

from fractions import Fraction
from pe_tools import cf_to_rational

def sum_of_digits(n):
    return sum(map(int, str(n)))


if __name__ == '__main__':
    e = [2]
    for i in range(1,40):
        e += [1, 2*i, 1]
    c = cf_to_rational(e[:100])
    print str(c)
    print "numerator sum: {}".format(sum_of_digits(c.numerator))
