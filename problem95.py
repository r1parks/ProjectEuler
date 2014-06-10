#!/usr/bin/env python

from pe_tools import approx_int_sqrt

divisor_sums = [0] * (10 ** 6 + 1)
numbers_to_test = set(range(2, 10 ** 6 + 1))

def divisor_sum(n):
    divisors = [1]
    for i in range(2, approx_int_sqrt(n)):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n / i)
    return sum(divisors)

def get_divisor_sum(n):
    ds = divisor_sums[n]
    if ds == 0:
        divisor_sums[n] = divisor_sum(n)
        if divisor_sums[n] > len(divisor_sums):
            divisor_sums[n] = -1
    return divisor_sums[n]

def divisor_sum_chain(n):
    global numbers_to_test
    chain = [n]
    next_n = get_divisor_sum(n)
    while next_n not in chain and next_n != -1:
        chain.append(next_n)
        next_n = get_divisor_sum(next_n)
    numbers_to_test -= set(chain)
    if next_n == -1:
        return []
    else:
        i = chain.index(next_n)
        return chain[i:]

if __name__ == '__main__':
    iterations = 0
    best = 0
    while len(numbers_to_test) > 0:
        iterations += 1
        next_num = numbers_to_test.pop()
        chain = divisor_sum_chain(next_num)
        if len(chain) > 0:
            assert chain[0] == divisor_sum(chain[-1])
        if len(chain) > best:
            best = len(chain)
            print "{}".format(min(chain))
    print "iterations: {}".format(iterations)
