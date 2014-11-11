#!/usr/bin/env python

def f(k, n):
    return sum(map(lambda x: pow(x, k), range(1, n+1)))

def S(k, n):
    return sum(f(k,i) for i in range(1,n+1))

def T(k, n, p):
    return S(k, n) % p

def testNewT(newT):
    for k in range(10, 12):
        for n in range(100,150):
            for p in [17,19,23]:
                if fastT(k,n,p) != newT(k,n,p):
                    raise Exception("{} failed on k={}, n={}, p={}".format(newT.__name__, k, n, p))

def fastT(k, n, p):
    total = 0
    stuff = zip(range(1, n+1), range(n, 0, -1))
    for i, scalar in stuff:
           total += (pow(i, k, p) * scalar) % p
    return total % p

def wtf_is_the_scalar(i, n, p):
    tmp = n - i + 1
    s = 0
    while tmp > 0:
        s += tmp
        tmp -= p
    return s

def superFastT(k, n, p):
    total = 0
    for i in xrange(1, p):
        scalar = wtf_is_the_scalar(i, n, p)
        total += (pow(i, k, p) * scalar) % p
    return total % p

def quick_scalar(i, n, p):
    s = n - i + 1
    iterations = (s/p) + 1
    ps_to_subtract = ((iterations - 1) * iterations) / 2
    return ((s * iterations) - (p * ps_to_subtract)) % p

def lightningT(k, n, p):
    total = 0
    for i in xrange(1, p):
        scalar = quick_scalar(i, n, p)
        total += (pow(i, k, p) * scalar) % p
    return total % p

def the_primes():
    from primes import find_next_prime
    next_prime = find_next_prime(2 * (10 ** 9))
    while next_prime < 2*(10 ** 9) + 2000:
        yield next_prime
        next_prime = find_next_prime(next_prime+1)

def sumT(p):
    print "next: {}".format(p)
    s = lightningT(10000, 10**12, p)
    return s

def parallelT(ps):
    from multiprocessing import Pool
    pool = Pool(processes = 7)
    return sum(pool.map(sumT, ps))

def bernouliiT(p):
    

def testSumT():
    ps = [7841, 7853, 7867, 7873, 7877, 7883, 7901, 7907, 7919, 5741, 5743, 6199, 6287, 6301, 4481, 4139, 5507]
    import time
    start = time.time()
    s1 = parallelT(ps)
    print "parallel took: {}".format(time.time() - start)
    start = time.time()
    s2 = sum(map(lambda p: lightningT(10000, 10**12, p), ps))
    print "non parallel took: {}".format(time.time() - start)
    assert s1 == s2

if __name__ == '__main__':
    testNewT(superFastT)
    testNewT(lightningT)
    testSumT()
    pgen = the_primes()
    ps = [p for p in pgen]
    print parallelT(ps)


#answer 106650212746
