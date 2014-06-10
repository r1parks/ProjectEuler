#!/usr/bin/env python

from pe_tools import memoized

possible_numbers = set(range(3, 10 ** 6))

def factorial(n):
    return reduce(lambda x, y: x * y, range(2, n+1), 1)

@memoized
def digit_factorial(n):
    return sum(map(factorial, map(int, str(n))))

def chain_length(n):
    chain = [n]
    next_num = digit_factorial(n)
    while next_num not in chain:
        chain.append(next_num)
        next_num = digit_factorial(next_num)
    return len(chain)

if __name__ == '__main__':
    total = 0
    while len(possible_numbers) > 0:
        next_num = possible_numbers.pop()
        if chain_length(next_num) == 60:
            total += 1
    print "total: {}".format(total)
