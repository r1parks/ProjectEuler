#!/usr/bin/env python

from primes import is_prime, get_huge_prime_set

primes = get_huge_prime_set()

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

def compute_factors(n):
    from itertools import chain
    from pe_tools import approx_int_sqrt
    if is_prime(n):
        return [n]
    s = approx_int_sqrt(n)
    for p in chain(primes, xrange(max(primes), s, 2)):
        if n % p == 0:
            return [n] + get_factors(n/p)
    raise Exception("Failed to factor {}".format(n))

def get_factors(n):
    if n >= len(factors):
        return compute_factors(n)
    if len(factors[n]) == 1:
        return factors[n]
    assert len(factors[n]) == 2
    if factors[n][0] == factors[n][1]:
        return factors[n]
    return [factors[n][0]] + get_factors(factors[n][1])

def phi_from_factors(facts):
    from collections import Counter
    total = 1
    facts_freq = Counter(facts)
    for p in facts_freq:
        k = facts_freq[p]
        total *= p ** (k-1) * (p-1)
    return total

def phi(n):
    return phi_from_factors(get_factors(n))

def S(n, m):
    n_factors = get_factors(n)
    total = 0
    for i in range(1, m+1):
        total += phi_from_factors(n_factors + get_factors(i))
    return total

if __name__ == '__main__':
    n = 510510
    m = 10 ** 6
    print "S({}, {}) = {}".format(n, m, S(n, m))
    print  "phi(510510 * 10**11 = {}".format(phi(510510 * 10 ** 11))
