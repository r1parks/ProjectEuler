#!/usr/bin/env python

import primes


PRIMES = None


def two_factor_sieve(numbers):
    maxes = {}
    for idx, number in enumerate(numbers):
        if number is None:
            continue
        assert idx == number, "{} {}".format(idx, number)
        factors = list(primes.factorGen(number))
        if len(factors) < 2:
            numbers[idx] = None
        if len(factors) > 2:
            while idx < len(numbers):
                numbers[idx] = None
                idx += number
        if len(factors) == 2:
            maxes[(factors[0][0], factors[1][0])] = number
    return maxes


def S(n):
    global PRIMES
    PRIMES = primes.primes_below(n / 2 + 1)
    all_numbers = list(range(n + 1))
    all_numbers[0] = None
    all_numbers[1] = None
    numbers_with_two_factors = two_factor_sieve(all_numbers)
    return sum(numbers_with_two_factors.values())


def main():
    print S(10000000)


if __name__ == '__main__':
    main()
