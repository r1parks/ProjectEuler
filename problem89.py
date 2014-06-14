#!/usr/bin/env python

numerals = [('I', 1),
            ('IV', 4),
            ('V', 5),
            ('IX', 9),
            ('X', 10),
            ('XL', 40),
            ('L', 50),
            ('XC', 90),
            ('C', 100),
            ('CD', 400),
            ('D', 500),
            ('CM', 900),
            ('M', 1000)]

def numeralToInt(n):
    for numeral, val in numerals[::-1]:
        if n.startswith(numeral):
            return val + numeralToInt(n[len(numeral):])
    return 0

def intToNumeral(i):
    for numeral, val in numerals[::-1]:
        if val <= i:
            return numeral + intToNumeral(i-val)
    return ''

def test():
    for i in range(1, 100000):
        if i != numeralToInt(intToNumeral(i)):
            print "First Failure:\n\t{} -> {} -> {}".format(i, intToNumeral(i), numeralToInt(intToNumeral(i)))
            break

if __name__ == '__main__':
    import fileinput
    total = 0
    for n in fileinput.input():
        n = n.strip()
        i = numeralToInt(n)
        n2 = intToNumeral(i)
        diff = len(n) - len(n2)
        total += diff
    print str(total)
