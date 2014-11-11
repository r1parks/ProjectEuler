#!/usr/bin/env python

import primes
from bisect import bisect_left

target = 50000000
all_primes = primes.get_medium_prime_set()
primes_squared = map(lambda x: x ** 2, all_primes[:bisect_left(all_primes, pow(target, 1/2.))])
primes_cubed = map(lambda x: x ** 3, all_primes[:bisect_left(all_primes, pow(target, 1/3.))])
primes_fourth_power = map(lambda x: x ** 4, all_primes[:bisect_left(all_primes, pow(target, 1/4.))])

all_sums = set()

for p4 in primes_fourth_power:
    for p3 in primes_cubed:
        if p3 + p4 >= target:
            break
        for p2 in primes_squared:
            if p2 + p3 + p4 >= target:
                break
            all_sums.add(p4 + p3 + p2)
print len(all_sums)
