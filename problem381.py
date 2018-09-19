#!/usr/bin/env python


def S_vals(p):
    next_val = -1 % p
    yield next_val
    for k in range(2, 6):
        next_val = (next_val * pow(p - k + 1, p - 2, p)) % p
        yield next_val


def S(p):
    return sum(S_vals(p)) % p


def AllS(limit):
    import primes
    for p in primes.primes_below(limit):
        if p < 5:
            continue
        yield S(p)


def main():
    print sum(AllS(10 ** 8))


if __name__ == '__main__':
    main()
