#!/usr/bin/env python

def is_square(n):
    h = n & 0xF
    if h in [0,1,4,9]:
        from math import sqrt
        s = int(sqrt(n))
        return n == s*s
    return False
    
def getXfromY(y, D):
    xsquared = 1 + D*y*y
    if xsquared > 0 and is_square(xsquared) and xsquared - D*y*y == 1:
        from math import sqrt
        return long(sqrt(xsquared))
    else:
        return 0

def getXY(D):
    y = 1
    x = getXfromY(y, D)
    while x == 0:
        y += 1
        x = getXfromY(y, D)
    return x, y

def run(Ds):
    newDs = Ds[:]
    bestD = 0
    biggestX = 0
    y = 1
    while True:
        for D in Ds:
            x = getXfromY(y, D)
            if x > 0:
                newDs.remove(D)
                print "D, x, y = {}, {}, {}".format(D, x, y)
                print "Best D, x = {}, {}".format(bestD, biggestX)
                print "{}".format(newDs)
            if x > biggestX:
                bestD = D
                biggestX = x
        Ds = newDs[:]
        y += 1

if __name__ == '__main__':
    run(range(2,1000))
