#!/usr/bin/env python

from pe_tools import nCr
from math import sqrt

raw_input()

def binomial_expand(n):
    terms = []
    for r in range(n+1):
        coefficient = nCr(n, r)
        first_exponent = n-r
        second_exponent = r
        terms.append((coefficient, first_exponent, second_exponent))
    return terms

def compute_thing(terms):
    a = 3
    b = 5
    int_term = 0
    irrational_term = 0
    for n in terms:
        s = (n[0]) * (3 ** n[1]) * (5 ** (n[2]/2))
        if n[2] % 2 == 0:
            int_term += s
        else:
            irrational_term += s
    #print "{} + {}*sqrt(5)".format(int_term, irrational_term)
    return int_term + irrational_term * sqrt(5)

case = 1
while True:
    try:
        n = int(raw_input())
    except:
        break
    terms = binomial_expand(n)
    solution = compute_thing(terms)
    str_solution = ("000" + str(int(solution)))[-3::]
    print "Case #{}: {}".format(case, str_solution)
    case += 1
