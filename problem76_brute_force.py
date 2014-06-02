#!/usr/bin/env python

from ast import literal_eval
from pe_tools import memoized

@memoized
def find_summations_recursive(n):
    if n == 1:
        return ["[1]"]
    summations = set()
    for i in range(1, n):
        for summation in find_summations_recursive(n-i):
            summation = literal_eval(summation)
            summations.add(str(sorted(summation + [i])))
        summations.add(str([n]))
    return list(summations)

def find_summations(n):
    all_summations = find_summations_recursive(n)
    return filter(lambda x: len(literal_eval(x)) > 1, all_summations)

if __name__ == '__main__':
    from time import time
    start_time = time()
    for n in range(1, 100):
        l = len(find_summations(n))
        total_time = time() - start_time
        print "{}:\t{}\t{:.3f}s\t>{:.4f}s remaining".format(n, l, total_time, total_time * (100-n))
        start_time = time()
