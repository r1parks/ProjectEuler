#!/usr/bin/env python

from fractions import gcd, Fraction

if __name__ == '__main__':
    max_d = 12000
    total = 0
    for d in range(2, max_d+1):
        n = d / 3 + 1
        while n * 2 < d:
            if gcd(n, d) == 1:
                total += 1
            n += 1
    print total
