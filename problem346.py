#!/usr/bin/env python


def sum_repuints(limit):
    strong_repunits = set([1])
    base = 2
    while base ** 2 + base + 1 < limit:
        next_strong_repunit = base ** 2 + base + 1
        while next_strong_repunit < limit:
            strong_repunits.add(next_strong_repunit)
            next_strong_repunit *= base
            next_strong_repunit += 1
        base += 1
    return sum(strong_repunits)


def main():
    print sum_repuints(10 ** 12)


if __name__ == '__main__':
    main()
