#!/usr/bin/env python

from itertools import permutations

def validate(outer, inner):
    if outer[0] != min(outer):
        return False
    total = outer[0] + inner[0] + inner[1]
    for i in range(len(outer)):
        if outer[i] + inner[i] + inner[(i+1)%len(inner)] != total:
            return False
    #s = "total: {}, ".format(total)
    print "tota: {}".format(total)
    s = ""
    for i in range(len(outer)):
        #s += "{} {} {} ".format(outer[i] + inner[i] + inner[(i+1)%len(inner)])
        s += str(outer[i])
        s += str(inner[i])
        s += str(inner[(i+1) % len(inner)])
    print s
    return True

def try_permutation(out_p, in_p):
    validate(out_p, in_p)

if __name__ == '__main__':
    for out_p in permutations(range(6,11)):
        for in_p in permutations(range(1,6)):
            validate(out_p, in_p)
