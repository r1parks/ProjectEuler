#!/usr/bin/env python

import primes
from bisect import bisect_left, bisect_right
from pe_tools import nCr, approx_int_sqrt

below_n = 10**8

def num_coprimes_with(p, relevant_primes):
    max_p = below_n / p
    assert(p <= max_p)
    return bisect_right(relevant_primes, max_p) - bisect_left(relevant_primes, p)

if __name__ == "__main__":
    relevant_primes = sorted(list(filter((lambda x: x < below_n), primes.get_huge_prime_set())))
    print sum(num_coprimes_with(n, relevant_primes) for n in relevant_primes[:bisect_right(relevant_primes, approx_int_sqrt(below_n))])
