#!/usr/bin/env python

from primes import is_prime

if __name__ == '__main__':
    distinct_factors = [0] * (10 ** 5 + 1)
    E = [0] * (10 ** 5 + 1)
    primes = [x for x in range(2, len(distinct_factors)) if is_prime(x)]

    distinct_factors[0] = set([0])
    distinct_factors[1] = set([1])

    for p in primes:
        distinct_factors[p] = set([p])

    def get_rad_list(i):
        if distinct_factors[i] == 0:
            for p in primes:
                if i % p == 0:
                    distinct_factors[i] = set([p])
                    distinct_factors[i].update(get_rad_list(i/p))
                    return distinct_factors[i]
        else:
            return distinct_factors[i]
        raise Exception("failed to factor: {}".format(i))

    def get_rad(i):
        from operator import mul
        return reduce(mul, get_rad_list(i), 1)

    for i in range(1, len(E)):
        E[i] = (i, get_rad(i))

    sorted_thing = sorted(E[1:], key=lambda x : x[1])
    print "{}".format(sorted_thing[10000-1][0])
    

