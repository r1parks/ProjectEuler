#!/usr/bin/env python

import fileinput
from pe_tools import cross_product, normal_vector

def create_triangle_from_line(input_line):
    tokens = map(int, input_line.strip().split(','))
    return [(tokens[i], tokens[i+1]) for i in range(0,len(tokens),2)]

def prep_input(input_lines):
    return map(create_triangle_from_line, input_lines)

def solve(triangle):
    origin = (0,0,0)
    p1, p2, p3 = triangle
    p1 = p1[0], p1[1], 0
    p2 = p2[0], p2[1], 0
    p3 = p3[0], p3[1], 0
    v1 = cross_product(normal_vector(p1, p2), normal_vector(p1, origin))[2]
    v2 = cross_product(normal_vector(p2, p3), normal_vector(p2, origin))[2]
    v3 = cross_product(normal_vector(p3, p1), normal_vector(p3, origin))[2]
    res =  (v1/abs(v1)) == (v2/abs(v2)) == (v3/abs(v3))
    return res

if __name__ == "__main__":
    input_lines = []
    for line in fileinput.input():
        input_lines.append(line)
    formatted_input = prep_input(input_lines)
    ans = len(filter(solve, formatted_input))
    print ans
