#!/usr/bin/env python


import primes
from pe_tools import memoized


factorGen = memoized(primes.factorGen)
limit = 10 ** 8
s_table = [0] * (limit + 1)
s_table[0] = 0
s_table[1] = 0


def s(n):
    if s_table[n] > 0:
        return s_table[n]
    return max(s(p ** e) for p, e in factorGen(n))


def prime_s_values(p):
    e = 1
    n = 1
    m = p
    while n < len(s_table):
        m = p * e
        next_factorial = m
        n *= p
        n_multiple = n
        while n_multiple < len(s_table):
            s_table[n_multiple] = max(s_table[n_multiple], m)
            n_multiple += n
        next_factorial /= p
        while next_factorial % p == 0:
            n *= p
            next_factorial /= p
        e += 1


def main():
    for p in primes.primes_below(limit):
        prime_s_values(p)
    print sum(s_table)


if __name__ == '__main__':
    main()
