#!/usr/bin/env python

from pe_tools import memoized

def pentagonal_number(k):
    return k * (3*k - 1) / 2

@memoized
def p(n):
    cache = [1,1,2,3,5,7,11]
    if n < len(cache):
        return cache[n]
    total = 0
    k = 1
    string = "p({}) = ".format(n)
    while True:
        for next_pent in (pentagonal_number(k), pentagonal_number(-k)):
            if next_pent > n:
                break
            sign = ((-1) ** (k-1))
            term = p(n - next_pent)
            total += sign * term
            string += '+' if sign > 0 else '-'
            string += 'p({})={} '.format(n-next_pent, term)
        if pentagonal_number(-k) > n:
            break
        k += 1
    string += '= {}'.format(total)
    return total

    
if __name__ == '__main__':
    i = 2
    while True:
        if i % 10000 == 0:
            print "{}".format(i)
        if p(i) % (10 ** 6) == 0:
            break
        i += 1
    print "{}".format(i)
