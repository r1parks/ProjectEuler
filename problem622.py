#!/usr/bin/env python


def next_position(p, deck):
    if p <= deck / 2:
        return p * 2 - 1
    else:
        return (p - deck / 2) * 2


def cycle_length(deck):
    p = next_position(2, deck)
    shuffles = 1
    while p != 2:
        p = next_position(p, deck)
        shuffles += 1
    return shuffles


def sum_cycle_lenghts(n):
    total = 0
    last_found = 0
    for deck in range(4, 2 ** (n + 1), 2):
        if cycle_length(deck) == n:
            total += deck
            print '\t{}'.format(deck - last_found)
            last_found = deck
    return total


def main():
    for n in range(4, 25, 2):
        print n
        sum_cycle_lenghts(n)


if __name__ == '__main__':
    main()
