#!/usr/bin/env python

import math
import pe_tools

def approx_int_sqrt(n):
    return int(math.sqrt(n))

def continued_fraction_sqrt(n):
    a = a0 = approx_int_sqrt(n)
    m = 0
    d = 1
    sequence = []
    while True:
        m = d*a - m
        d = (n - m*m) / d
        a = (a0 + m) / d
        next_triple = (a, d, m)
        if next_triple in sequence:
            return len(sequence)
        sequence.append(next_triple)

if __name__ == '__main__':
    total = 0
    for i in range(1, 10000):
        if not pe_tools.is_square(i):
            l = continued_fraction_sqrt(i)
            #print "n, l = {}".format((i, l))
            if l % 2 == 1:
                total+=1
    print str(total)
