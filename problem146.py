#!/usr/bin/env python

from gmpy import is_prime

def fits_prime_pattern(n):
    nsquared = n * n
    if nsquared + 1 % 2 == 0:
        return False
    return (is_prime(nsquared + 1) and
           is_prime(nsquared + 3) and
           not is_prime(nsquared + 5) and
           is_prime(nsquared + 7) and
           is_prime(nsquared + 9) and
           not is_prime(nsquared + 11) and
           is_prime(nsquared + 13) and
           not is_prime(nsquared + 15) and
           not is_prime(nsquared + 17) and
           not is_prime(nsquared + 19) and
           not is_prime(nsquared + 21) and
           not is_prime(nsquared + 23) and
           not is_prime(nsquared + 25) and
           is_prime(nsquared + 27))

if __name__ == '__main__':
    total = 0
    n = 10
    while n < 150000000:
        if fits_prime_pattern(n):
            print str(n)
            total += n
            n += 10
        n += 10
    print "total: {}".format(str(total))
        
