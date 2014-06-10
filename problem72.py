#!/usr/bin/env python

from primes import is_prime

primes = [x for x in range(1000) if is_prime(x)]

factors = [0] * (10 ** 6 + 1)

def set_factors():
    for i in range(len(factors)):
        if i < 4 or is_prime(i):
            factors[i] = [i]
            continue
        for p in primes:
            if i % p == 0:
                factors[i] = [p, i/p]
                break

set_factors()

def get_factors(n):
    if len(factors[n]) == 1:
        return set(factors[n])
    assert len(factors[n]) == 2
    if factors[n][0] == factors[n][1]:
        return set(factors[n])
    return set([factors[n][0]] + list(get_factors(factors[n][1])))

def phi(n):
    p = n
    facts = get_factors(n)
    for fact in facts:
        p *= 1 - (1.0/fact)
    return int(round(p))

if __name__ == '__main__':
    total = 0
    for i in range(2, 1000000+1):
        total += phi(i)
    print "{}".format(total)
