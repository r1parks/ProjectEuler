#!/usr/bin/env python

from primes import smallFactorGen, primes_below

def smallPhi(n):
    phi = 1
    factors = smallFactorGen(n)
    for factor in factors:
        p,k = factor
        phi *= p**(k-1) * (p-1)
    return phi

def R(d):
    return smallPhi(d) / float(d-1)

def print_best(d):
    target = 15499 / 94744.
    print "d: {}, R(d) = {}, diff = {}".format(d, R(d), R(d) - target)

if __name__ == '__main__':
    target = 15499 / 94744.
    best = 99999999999999999999999
    d = 1
    for p in primes_below(50):
        d *= p
        if R(d) - target < 0:
            best = d
            print_best(d)
            d /= p
            break
    for m in range(2, 100000):
        new_d = d * m
        if R(new_d) < target and new_d < best:
            print_best(new_d)
            best = new_d
