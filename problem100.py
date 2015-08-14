#!/usr/bin/env python

from itertools import count
from math import sqrt
from pe_tools import is_square

def good_solution(x, b):
    return 2*b**2 - 2*b == x**2 - x

def solve_quadratic(a, b, c):
    solutions = []
    d = b**2 - 4*a*c
    if d == 0:
        solutions.append((-b + sqrt(d)) / (2*a))
    elif d > 0:
        solutions.append((-b + sqrt(d)) / (2*a))
        solutions.append((-b - sqrt(d)) / (2*a))
    return solutions

def blue_disks(x):
    a,b = 2,-2
    c = - (x**2 - x)
    if is_square(4 - 8 * c):
        possible_solutions = solve_quadratic(a, b, c)
        for b in possible_solutions:
            if good_solution(x, round(b)):
                return long(b)
    return 0

if __name__ == '__main__':
    for x in count(10**12):
        b = blue_disks(x)
        if b != 0:
            print "x={}, b={}".format(x, b)
