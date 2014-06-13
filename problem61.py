#!/usr/bin/env python

triangular_numbers = set([n * (n-1) / 2 for n in range(1,150)])
square_numbers = set([n * n for n in range(1, 101)])
pent_numbers = set([n * (3*n - 1) / 2  for n in range(1,90)])
hex_numbers = set([n * (2*n - 1) for n in range(1,80)])
hept_numbers = set([n * (5*n - 3) / 2 for n in range(1,70)])
oct_numbers = set([n * (3*n - 2) for n in range(1,60)])

def make_lookup(numbers):
    lookup = {}
    for num in numbers:
        if num > 9999 or num < 1000:
            continue
        n = str(num)
        assert(len(n) == 4)
        try:
            lookup[n[:2]].append(n)
        except:
            lookup[n[:2]] = [n]
    return lookup

def make_set(numbers):
    num_set = set()
    for num in numbers:
        if num > 9999 or num < 1000:
            continue
        n = str(num)
        assert(len(n) == 4)
        num_set.add(n)
    return num_set

tri_set = make_set(triangular_numbers)
square_lookup = make_lookup(square_numbers)
pent_lookup = make_lookup(pent_numbers)
hex_lookup = make_lookup(hex_numbers)
hept_lookup = make_lookup(hept_numbers)
oct_lookup = make_lookup(oct_numbers)

def find_sequence(sub_sequence, remaining_sets):
    first_two_digits = sub_sequence[-1][2:]
    if len(remaining_sets) == 0:
        if first_two_digits == sub_sequence[0][:2]:
            return sub_sequence
        else:
            return None
    for i in range(len(remaining_sets)):
        next_set = remaining_sets[i]
        possible_next_numbers = next_set.get(first_two_digits, [])
        for next_num in possible_next_numbers:
            result = find_sequence(sub_sequence + [next_num], remaining_sets[:i] + remaining_sets[i+1:])
            if result:
                return result

if __name__ == '__main__':
    sets = [square_lookup, pent_lookup, hex_lookup, hept_lookup, oct_lookup]
    for n in tri_set:
        s = find_sequence([n], sets)
        if s:
            print "sum: {}".format(sum(map(int, s)))
            import sys; sys.exit(0)
