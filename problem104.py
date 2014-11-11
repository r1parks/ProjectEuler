#!/usr/bin/env python

def is_pandigital(sn):
    if len(sn) < 9:
        return False
    if len(sn) > 9:
        raise Exception("len({}) > 9".format(sn))
    for d in range(1,10):
        if str(d) not in sn:
            return False
    else:
        return True

def test():
    assert(is_pandigital(str(123456789)))
    assert(is_pandigital(str(134652879)))
    assert(is_pandigital(str(341265897)))
    assert(is_pandigital(str(314526879)))
    assert(is_pandigital(str(531842679)))
    assert(not is_pandigital(str(31842679)))
    assert(not is_pandigital(str(38244679)))
    assert(not is_pandigital(str(352884679)))
    assert(not is_pandigital(str(352887669)))

def fib_gen():
    fib = [1,1]
    n = 2
    next_n = 2
    while True:
        if n == next_n:
            next_n = yield fib[1]
            if next_n == None:
                next_n = n + 1
        n += 1
        fib = fib[1], fib[0] + fib[1]

def find_fib_big():
    fg = fib_gen()
    fg.next()
    fib = [1, 1]
    n = 2
    while True:
        n += 1
        fib = fib[1], (fib[0] + fib[1]) % 10**9
        if is_pandigital(str(fib[1])):
            big_fib = fg.send(n)
            if is_pandigital(str(big_fib)[:9]):
                return n

if __name__ == '__main__':
    test()
    print find_fib_big()
