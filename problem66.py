#!/usr/bin/env python

"""
int PerfectSquare(int n)
{
    int h = n & 0xF; // last hexidecimal "digit"
    if (h > 9)
        return 0; // return immediately in 6 cases out of 16.

    // Take advantage of Boolean short-circuit evaluation
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {
        // take square root if you must
        int t = (int) floor( sqrt((double) n) + 0.5 );
            return t*t == n;
    }
    return 0;
}
"""

def is_square(n):
    h = n & 0xF
    if h in [0,1,4,9]:
        from math import sqrt
        s = int(sqrt(n))
        return n == s*s
    return False

def getY(x, D):
    search = [1,x]
    while search[0] < search[1]:
        y = (search[1] - search[0]) / 2 + search[0]
        if y == search[0]:
            break
        fx = x*x - D*y*y
        if fx == 1:
            return y
        if fx < 1:
            search = [search[0], y]
        else:
            search = [y, search[1]]
    return None

def getX(D):
    x = 1
    while getY(x, D) == None:
        x += 1
        if x % 10000 == 0:
            print "trying x: {}".format(x)
    return x

if __name__ == '__main__':
    bestD = 0
    biggestX = 0
    for D in range(1, 1000):
        if is_square(D):
            continue
        print "current D: {}".format(D)
        x = getX(D)
        if x > biggestX:
            print "new x: {}".format(x)
            print "new D: {}".format(D)
            biggestX = x
            bestD = D
    print "new x: {}".format(x)
    print "new D: {}".format(D)
    print "Done :)"
