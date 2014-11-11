#!/usr/bin/env python

from pe_tools import memoized

def isIncreasing(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def isDecreasing(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            return False
    return True

def isBouncy(n):
    return not (isIncreasing(n) or isDecreasing(n))

@memoized
def bouncyBelow(n):
    if n < 100:
        return 0
    if n == 1000:
        return 525 #given in the problem
    return bouncyBelow(n-1) + int(isBouncy(n))

def bouncyRatio(n):
    return float(bouncyBelow(n)) / float(n)

if __name__ == '__main__':
    from itertools import count
    for i in count(1000):
        if bouncyRatio(i) >= 0.99:
            print "{}".format(i)
            break
