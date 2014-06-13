#!/usr/bin/env python

from pe_tools import repeating_cf, continued_fraction_sqrt, cf_to_rational, is_square

def test_pells_equation(x, d, y):
    return x*x - d*y*y == 1

def solve_pells_for_x(d):
    i = 1
    while True:
        cf = repeating_cf(continued_fraction_sqrt(d))
        finite_cf = [cf.next() for _ in range(i)]
        rational = cf_to_rational(finite_cf)
        if test_pells_equation(rational.numerator, d, rational.denominator):
            return rational.numerator
        i += 1

if __name__ == '__main__':
    bestD = 0
    bestX = 0
    for d in range(2, 1000):
        if is_square(d):
            continue
        x = solve_pells_for_x(d)
        if x > bestX:
            bestD = d
            bestX = x
    print "{}".format(bestD)
