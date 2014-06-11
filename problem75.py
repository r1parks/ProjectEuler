#!/usr/bin/env python

from pe_tools import approx_int_sqrt
from fractions import gcd
from itertools import count

max_total = 1500000
triples = [0] * (max_total+1)

def get_answer():
    for n in range(1, approx_int_sqrt(max_total)):
        for m in range(n+1, max_total/n, 2):
            if gcd(m,n) != 1:
                continue
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            if a + b + c > max_total:
                break
            assert(a*a + b*b == c*c)
            for k in count(1):
                ka = k*a
                kb = k*b
                kc = k*c
                if ka + kb + kc > max_total:
                    break
                assert ka**2 + kb**2 == kc**2
                triples[ka+kb+kc] += 1
    print "{}".format(len(filter(lambda x: x == 1, triples)))

if __name__ == '__main__':
    get_answer()
