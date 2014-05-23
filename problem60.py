#!/usr/bin/env python

import primes
import sys

def split_prime(p):
    str_p = "{}".format(p)
    for i in range(1, len(str_p)):
        p1, p2 = long(str_p[:i]), long(str_p[i:])
        if primes.is_prime(long(p1)) and primes.is_prime(long(p2)) and primes.is_prime(long("{}{}".format(p2, p1))):
            return [p1, p2]

def try_prime_pair(p1, p2):
    return primes.is_prime(long("{}{}".format(p1,p2))) and primes.is_prime(long("{}{}".format(p2,p1)))

def try_prime_test(possible_set):
    ps = list(possible_set)
    for i in range(len(ps)):
        for j in range(i+1, len(ps)):
            if not try_prime_pair(ps[i], ps[j]):
                return False
    return True

def add_new_primes(new, old):
    if frozenset(new) in old:
        return
    new_sets = [frozenset(new)]
    for prime_set in old:
        possible_set = prime_set.union(new)
        if possible_set not in old and possible_set not in new_sets and try_prime_test(possible_set):
            new_sets.append(possible_set)
            if len(possible_set) == 5:
                print possible_set
                sys.exit(0)
    old.update(new_sets)

if __name__ == '__main__':
    prime_sets = set()
    current_prime = 10
    while True:
        current_prime = primes.find_next_prime(current_prime + 1)
        new_primes = split_prime(current_prime)
        if new_primes:
            add_new_primes(new_primes, prime_sets)
