#!/usr/bin/env python


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True  # n  is definitely composite


def miller_rabin(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if miller_rabin(x)]


def is_prime(n):
    if n < 2:
        return False
    else:
        return miller_rabin(n)


def find_next_prime(n):
    if n <= 2:
        return 2
    n += 1 if n % 2 == 0 else 0
    while is_prime(n) is False:
        n += 2
    return n


def prime_generator(n=2):
    if n <= 2:
        yield 2
    n += 1 if n % 2 == 0 else 0
    while is_prime(n) is False:
        n += 2
    yield n


def get_huge_prime_set():
    if get_huge_prime_set._cache is not None:
        return get_huge_prime_set._cache
    import cPickle as pickle
    prime_file_name = 'prime_list.pickle'
    try:
        with open(prime_file_name, 'rb') as prime_file:
            print "File open, reading in pickle"
            primes = pickle.load(prime_file)
            print "File loaded :)"
    except:
        print "Prime file not found, creating one now! (This will take a minute...)"
        primes = []
        p = 1
        for i in xrange(10000000):
            p = find_next_prime(p + 1)
            if i % 10000 == 0:
                print "prime number {:,}: {:,}".format(i, p)
            primes.append(p)
        with open(prime_file_name, 'wb') as prime_file:
            pickle.dump(primes, prime_file)
    get_huge_prime_set._cache = primes
    return primes


get_huge_prime_set._cache = None


def get_medium_prime_set():
    if get_medium_prime_set._cache is not None:
        return get_medium_prime_set._cache
    import cPickle as pickle
    prime_file_name = 'prime_list_medium.pickle'
    try:
        with open(prime_file_name, 'rb') as prime_file:
            print "File open, reading in pickle"
            primes = pickle.load(prime_file)
            print "File loaded :)"
    except:
        print "Prime file not found, creating one now! (This will take a minute...)"
        primes = []
        p = 1
        for i in xrange(100000):
            p = find_next_prime(p + 1)
            if i % 10000 == 0:
                print "prime number {:,}: {:,}".format(i, p)
            primes.append(p)
        with open(prime_file_name, 'wb') as prime_file:
            pickle.dump(primes, prime_file)
    get_medium_prime_set._cache = primes
    return primes


get_medium_prime_set._cache = None


def primes_below(n):
    from bisect import bisect_left
    if n < 1000:
        pset = _known_primes
    else:
        pset = get_medium_prime_set()
        if pset[-1] < n:
            pset = get_huge_prime_set()
    return pset[:bisect_left(pset, n + 1)]


def factorGen(n):
    assert n > 1
    import math
    prime_cache = primes_below(int(math.sqrt(n)))[::-1]
    p = 0
    while n > 1 and len(prime_cache) > 0:
        p = prime_cache.pop()
        if n % p == 0:
            rv = 0
            while n % p == 0:
                rv += 1
                n = n / p
            yield (p, rv)
            if is_prime(n):
                yield (n, 1)
                return
    if n > 1:
        yield (n, 1)


def smallFactorGen(n):
    assert n > 1
    prime_cache = primes_below(100)[::-1]
    p = 0
    while n > 1 and len(prime_cache) > 0:
        p = prime_cache.pop()
        if n % p == 0:
            rv = 0
            while n % p == 0:
                rv += 1
                n = n / p
            yield (p, rv)
            if is_prime(n):
                yield (n, 1)
                return
    if n > 1:
        yield (n, 1)


if __name__ == '__main__':
    for i in xrange(10000000000, 100000000000, 27):
        g = list(factorGen(i))
        total = 1
        for f in g:
            total *= f[0] ** f[1]
        if total != i:
            import pdb
            pdb.set_trace()
