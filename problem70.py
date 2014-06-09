#!/usr/bin/env python
from pe_tools import memoized
from primes import is_prime

primes = [x for x in range(10000) if is_prime(x)]

factors = [0] * 10 ** 7

def set_factors():
    for i in range(len(factors)):
        if i < 4 or is_prime(i):
            factors[i] = [i]
            continue
        for p in primes:
            if i % p == 0:
                factors[i] = [p, i/p]
                break

def get_factors(n):
    if len(factors[n]) == 1:
        return set(factors[n])
    assert len(factors[n]) == 2
    if factors[n][0] == factors[n][1]:
        return set(factors[n])
    return set([factors[n][0]] + list(get_factors(factors[n][1])))

def is_permutation(x, y):
    from collections import Counter
    return Counter(str(x)) == Counter(str(y))

def phi(n):
    p = n
    facts = get_factors(n)
    for fact in facts:
        p *= 1 - (1.0/fact)
    return int(round(p))

if __name__ == '__main__':
    best = 99999999999.0
    set_factors()
    for i in range(10, len(factors)):
        p = phi(i)
        if is_permutation(i, p):
            if i / float(p) < best:
                best = i / float(p)
                print "{}: {}".format(i, p)
