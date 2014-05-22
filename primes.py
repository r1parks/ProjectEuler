import random

def miller_rabin(n, k):
    assert(n > 3)
    assert(k > 0)
    assert(n > k+4)
    if pow(2, n-1, n) != 1:
        return False
    d = n-1
    s = 0
    while d % 2 == 0:
        d /= 2
        s += 1
    bases = set()
    while len(bases) < k:
        new_base = random.randrange(2, n-2)
        bases.add(new_base)
    for a in bases:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        return False
    return True

small_primes = set()
small_primes.update([2,3,5,7,11,13,17,19,23])

def is_prime(n):
    return (n in small_primes) or miller_rabin(n, 10)

def find_next_prime(n):
    n += 6 - ((n - 1) % 6)
    while is_prime(n) != True:
        n += 6
    return n

if __name__ == '__main__':
    p = find_next_prime(2 ** 10)
    print '{}'.format(p)
