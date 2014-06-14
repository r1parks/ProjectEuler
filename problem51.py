#!/usr/bin/env python

from primes import find_next_prime
from collections import Counter
from itertools import count
import re

p_map = {}

def createIndices(ps, c, v):
    indices = []
    for n in range(1, 2**v):
        bstr = "{:b}".format(n).zfill(v)
        index = ''
        for d in ps:
            if d == c:
                if bstr[0] == '1':
                    d = '.'       
                bstr = bstr[1:]
            index = index + d
        indices.append(index)
    return indices

def addGroup(p):
    group_size = 0
    best = ''
    ps = str(p)
    count = Counter(ps)
    for c, v in count.most_common():
        if v < 2:
            break
        indices = createIndices(ps, c, v)
        for index in indices:
            p_map.setdefault(index, []).append(p)
            if len(p_map[index]) > group_size:
                group_size = len(p_map[index])
                best = index
    return best

if __name__ == '__main__':
    n = 0
    for _ in count(0):
        n = find_next_prime(n+1)
        group = addGroup(n)
        if group and len(p_map[group]) == 8:
            print "{}".format(sorted(p_map[group])[0])
            break

