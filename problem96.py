#!/usr/bin/env python

import itertools
import fileinput
import multiprocessing

def validate(puzzle):
    assert len(puzzle) == 9
    assert all(map(lambda x: len(x) == 9, puzzle))
    assert all(map(lambda x: map(lambda n: n in range(10), x), puzzle))
    for n in range(len(puzzle)):
        rowx = xrow(puzzle, n)
        rowy = yrow(puzzle, n)
        assert len(set(rowx)) == len(rowx)
        assert len(set(rowy)) == len(rowy)
    for x,y in itertools.product((1,4,7),(1,4,7)):
        s = square(puzzle, x, y)
        assert len(set(s)) == len(s)

def format_input(input_raw):
    formatted_input = []
    while input_raw:
        formatted_input.append(tuple(map(lambda x: tuple(map(int, x)), input_raw[1:10])))
        input_raw = input_raw[10:]
    output = tuple(formatted_input)
    return output

is_zero = lambda n : n == 0
not_zero = lambda n : not is_zero(n)
combine = lambda x, y: x + y

def square(puzzle, x, y):
    x1, y1 = (x/3) * 3, (y/3) * 3
    output = filter(not_zero, (puzzle[x][y] for x in range(x1, x1+3) for y in range(y1, y1+3)))
    return sorted(list(output))

def xrow(puzzle, x):
    return sorted(list(filter(not_zero, puzzle[x])))

def yrow(puzzle, y):
    return sorted(filter(not_zero, (puzzle[x][y] for x in range(9))))

def possible_solutions(p, x, y):
    all_possible = set(range(1, 10))
    return all_possible - set(square(p,x,y)) - set(xrow(p,x)) - set(yrow(p,y))

def is_solved(puzzle):
    validate(puzzle)
    for x,y in itertools.product(range(len(puzzle)), range(len(puzzle[0]))):
        if puzzle[x][y] == 0:
            return False
        a = set(range(1, 10))
        s = set(xrow(puzzle, x))
        if not (s <= a and s >= a):
            return False
        s = set(yrow(puzzle, y))
        if not (s <= a and s >= a):
            return False
        s = set(square(puzzle, x, y))
        if not (s <= a and s >= a):
            return False
    return True

def updated(puzzle, x, y, n):
    validate(puzzle)
    if puzzle[x][y] == n:
        return puzzle
    new_row = ((puzzle[x][:y] + (n,) + puzzle[x][y+1:]),)
    new_puzzle = puzzle[0:x] + new_row + puzzle[x+1:]
    validate(new_puzzle)
    return new_puzzle

def best_open_squares(puzzle):
    open_squares = []
    for x,y in itertools.product(range(9), range(9)):
        if puzzle[x][y] == 0:
            open_squares.append((x,y,possible_solutions(puzzle, x, y)))
    return sorted(open_squares, key=lambda t: len(t[2]))

def best_open_square(puzzle):
    squares = best_open_squares(puzzle)
    return squares[0]

def backtrack(puzzle):
    if is_solved(puzzle):
        return puzzle
    x,y,p = best_open_square(puzzle)
    if len(p) == 0:
        return None
    for n in p:
        new_puz = backtrack(updated(puzzle, x, y, n))
        if new_puz is not None:
            return new_puz
    return None

def solve(puzzle):
    puzzle = backtrack(puzzle)
    if puzzle is not None:
        assert is_solved(puzzle)
        output = puzzle[0][0] * 100 + puzzle[0][1] * 10 + puzzle[0][2]
        print "{} -> {}".format(puzzle[0], output)
        return output
    else:
        print "something went wrong :/"

if __name__ == '__main__':
    input_raw = [line.strip() for line in fileinput.input()]
    formatted_input = format_input(input_raw)
    pool = multiprocessing.Pool(8)
    solutions = map(solve, formatted_input)
    print reduce(combine, solutions)
