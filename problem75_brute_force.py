#!/usr/bin/env python

Ls_to_try = set(range(3, 1500000+1))

def remove_all(L):
    global Ls_to_try
    n = L
    ns = []
    while n <= 1500000:
        ns.append(n)
        n += L
    Ls_to_try -= set(ns)

from math import sqrt, ceil
magic_ratio = sqrt(2) / (2.0 + sqrt(2))

if __name__ == '__main__':
    total = 0
    L = Ls_to_try.pop()
    while len(Ls_to_try) > 0:
        Ltotal = 0
        c = int(ceil(magic_ratio * L))
        for a in range(1, L/3):
            b = (L - a) / 2
            c = L - a - b
            while a*a + b*b > c*c:
                b -= 1
            if a*a + b*b == c*c:
                Ltotal+=1
                if Ltotal > 1:
                    remove_all(L)
                    break
        if Ltotal == 1:
            total += 1
        L = Ls_to_try.pop()
        print "L: {}, total: {}".format(L, total)
