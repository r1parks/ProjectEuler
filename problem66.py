#!/usr/bin/env python

import pe_tools

def repeating_cf(cf):
    assert len(cf) > 1
    yield cf[0]
    cf = cf[1:]
    i = 0
    while True:
        yield cf[i]
        i = (i + 1) % len(cf)

def test_pells_equation(x, d, y):
    return x*x - d*y*y == 1

def solve_pells_for_x(d):
    i = 1
    while True:
        cf = repeating_cf(pe_tools.continued_fraction_sqrt(d))
        finite_cf = [cf.next() for _ in range(i)]
        rational = pe_tools.cf_to_rational(finite_cf)
        if test_pells_equation(rational.numerator, d, rational.denominator):
            return rational.numerator
        i += 1

if __name__ == '__main__':
    bestD = 0
    bestX = 0
    for d in range(2, 1000):
        if pe_tools.is_square(d):
            continue
        x = solve_pells_for_x(d)
        if x > bestX:
            bestD = d
            bestX = x
    print "Best D: {}".format(bestD)
    print "Best x: {}".format(bestX)
