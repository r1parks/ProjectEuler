#!/usr/bin/env python

from bigfloat import sqrt, precision
from pe_tools import is_square

def hundred_digit_sum(n):
    s = str(n)
    if '.' in s:
        i = s.find('.')
        s = s[:i] + s[i+1:]
    s = s[:100]
    return sum(map(int, s))

if __name__ == '__main__':
    total = 0
    for n in range(1, 100):
        if not is_square(n):
            s = hundred_digit_sum(sqrt(n, precision(340)))
            total += s
    print str(total)
