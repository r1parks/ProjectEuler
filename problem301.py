#!/usr/bin/env python


def lose_nim(n):
    return 1 if n ^ n * 2 ^ n * 3 == 0 else 0


def solve_recursively(start, n):
    if int(start, 2) > 2 ** n:
        return 0
    sub_total = 1
    sub_total += solve_recursively(start + '0', n)
    if start[-1] == '0':
        sub_total += solve_recursively(start + '1', n)
    return sub_total


def main():
    print solve_recursively('1', 30)


if __name__ == '__main__':
    main()
