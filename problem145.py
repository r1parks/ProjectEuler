#!/usr/bin/env python

def all_odd_digits(n):
    while n > 0:
        if n % 2 == 0:
            return False
        n /= 10
    return True

def sanity_check(digits):
    if digits[0] == 0 or digits[-1] == 0:
        return False
    fwd = 0
    rev = 0
    for d1, d2 in zip(digits, digits[::-1]):
        fwd *= 10
        fwd += d1
        rev *= 10
        rev += d2
    s = fwd + rev
    all_odd = all_odd_digits(s)
    #print "digits: {}, fwd: {}, rev: {} sum: {}, all odd: {}".format(digits, fwd, rev, s, all_odd)
    return all_odd

def valid(digits):
    if digits[0] == 0 or digits[-1] == 0:
        return False
    rev_digits = digits[::-1]
    carry = 0
    for i in range(0, len(digits)):
        if digits[i] == -1 or rev_digits[i] == -1:
            break
        next_sum = digits[i] + rev_digits[i] + carry
        if next_sum % 2 == 0:
            return False
        carry = next_sum / 10
        assert(carry == 0 or carry == 1)
    return True

def get_reversable_total(n, i=0):
    if -1 not in n:
        #print "{}".format(n)
        return 1 if valid(n) else 0
    total = 0
    if len(n) % 2 == 1 and i == len(n) / 2: #middle digit
        for d in range(10):
            n[i] = d
            total += get_reversable_total(n, i+1)
        n[i] = -1
        return total
    for d1 in range(10):
        for d2 in range(10):
            n[i] = d1
            n[-(i+1)] = d2
            if valid(n):
                total += get_reversable_total(n, i+1)
        n[-(i+1)] = -1
    n[i] = -1
    return total

def reversable_of_len(l):
    return get_reversable_total([-1] * l)

if __name__ == '__main__':
    max_len = 8
    total = 0
    for l in range(2, max_len+1):
        total += reversable_of_len(l)
    print "total: {}".format(total)
