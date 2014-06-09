#!/usr/bin/env python

import primes
from ast import literal_eval
from pe_tools import memoized

known_primes = [x for x in range(10000) if primes.is_prime(x)]

@memoized
def find_prime_summations(n):
    if n == 2:
        return ['[2]']
    summations = set()
    i = 0
    while known_primes[i] < n-1:
        next_prime = known_primes[i]
        for summation in find_prime_summations(n - next_prime):
            summation = literal_eval(summation)
            summations.add(str(sorted(summation + [next_prime])))
        i += 1
    if primes.is_prime(n):
        summations.add(str([n]))
    return list(summations)

if __name__ == '__main__':
    i = 10
    l = len(find_prime_summations(i))
    while l < 5000:
        i += 1
        l = len(find_prime_summations(i))
    print i
