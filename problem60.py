#!/usr/bin/env python

import primes

def split_prime(p):
    """ attempts to split the prime into two primes """
    str_p = "{}".format(p)
    split_primes = []
    for i in range(1, len(str_p)):
        p1, p2 = long(str_p[:i]), long(str_p[i:])
        if primes.is_prime(long(p1) and primes.is_prime(long(p2))):
            split_primes.append((p1, p2))
    return set(split_primes)

if __name__ == '__main__':
    prime_sets = []
    current_prime = 10
    while True:
        current_prime = primes.find_next_prime(current_prime + 1)
        print "next prime: {}".format(current_prime)
