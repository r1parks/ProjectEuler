#!/usr/bin/env python

from pe_tools import nCr

if __name__ == '__main__':
    current_best = 0
    diff = 999999
    tgt = 2000000
    for w in range(2, 2000):
        h = 1
        recs = 0
        while recs < tgt and h <= w:
            recs = nCr(w+1, 2) * nCr(h+1, 2)
            if abs(tgt - recs) < diff:
                current_best = h * w
                diff = abs(tgt - recs)
                print "h = {}, w = {}, rectangles = {}, diff = {}".format(h, w, recs, diff)
            h += 1
    print current_best
        
