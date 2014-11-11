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

def dbg_print(puzzle, nx, ny):
    print "----"
    for x in range(len(puzzle)):
        row = ""
        for y in range(len(puzzle[x])):
            row += "{}".format(puzzle[x][y])
            row += "<-" if y==ny and x==nx else "  "
            if y % 3 == 2:
                row += "  "
        print row
        if x % 3 == 2:
            print ""
    print "x, y = {}, {}".format(nx, ny)
    print "xrow: {}".format(xrow(puzzle, nx))
    print "yrow: {}".format(yrow(puzzle, ny))
    print "sqre: {}".format(square(puzzle, nx, ny))
    print "posb: {}".format(possible_solutions(puzzle, nx, ny))

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

def xrow_possible(puzzle, x0, y):
    possible = set()
    for x in range(9):
        if x == x0:
            continue
        possible.update(possible_solutions(puzzle, x, y))
    return possible

def yrow_possible(puzzle, x, y0):
    possible = set()
    for y in range(9):
        if y == y0:
            continue
        possible.update(possible_solutions(puzzle, x, y))
    return possible

def square_possible(puzzle, x, y):
    return []

def hard_square(puzzle, x, y):
    my_possible = set(possible_solutions(puzzle, x, y))
    peer_possible = set()
    peer_possible.update(xrow_possible(puzzle, x, y))
    peer_possible.update(yrow_possible(puzzle, x, y))
    peer_possible.update(square_possible(puzzle, x, y))
    only_possible = my_possible - peer_possible
    if len(only_possible) == 1:
        return only_possible.pop()
    return 0

def ez_square(puzzle, x, y):
    solutions = possible_solutions(puzzle, x, y)
    if len(solutions) == 1:
        return solutions.pop()
    if len(solutions) == 0:
        return -1
    return 0

def zeros(puzzle):
    validate(puzzle)
    return sum(map(lambda row : len(filter(is_zero, row)), puzzle))

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

def solve_easy_squares(puzzle):
    for x in range(9):
        for y in range(9):
            if not_zero(puzzle[x][y]):
                continue
            n = ez_square(puzzle, x, y)
            if n == -1: #invalid square
                return puzzle
            if n == 0:
                n = hard_square(puzzle, x, y)
            puzzle = updated(puzzle, x, y, n)
    return puzzle

def find_best_square(puzzle):
    for x in range(len(puzzle)):
        for y in range(len(puzzle[x])):
            if puzzle[x][y] == 0:
                return x, y
    return -1, -1

def updated(puzzle, x, y, n):
    validate(puzzle)
    if puzzle[x][y] == n:
        return puzzle
    new_row = ((puzzle[x][:y] + (n,) + puzzle[x][y+1:]),)
    new_puzzle = puzzle[0:x] + new_row + puzzle[x+1:]
    validate(new_puzzle)
    return new_puzzle

def try_easy_solve(puzzle):
    while not is_solved(puzzle):
        original_spaces_left = zeros(puzzle)
        puzzle = solve_easy_squares(puzzle)
        if zeros(puzzle) == original_spaces_left:
            break
    return puzzle

def best_open_squares(puzzle):
    open_squares = []
    for x,y in itertools.product(range(9), range(9)):
        if puzzle[x][y] == 0:
            open_squares.append((x,y,possible_solutions(puzzle, x, y)))
    return sorted(open_squares, key=lambda t: len(t[2]))

def best_open_square(puzzle):
    squares = best_open_squares(puzzle)
    return squares[0]

def try_hard_solve(puzzle):
    if is_solved(puzzle):
        return puzzle
    for x, y in itertools.product(range(len(puzzle)), range(len(puzzle[0]))):
        if puzzle[x][y] != 0:
            continue
        for n in possible_solutions(puzzle, x, y):
            test_puzzle = updated(puzzle, x, y, n)
            test_puzzle = try_easy_solve(test_puzzle)
            if is_solved(test_puzzle):
                return test_puzzle
    return puzzle

def try_even_harder(puzzle):
    if is_solved(puzzle):
        return puzzle
    for x,y,p in best_open_squares(puzzle):
        for n in p:
            test_puzzle = updated(puzzle, x, y, n)
            #dbg_print(puzzle, x, y)
            test_puzzle = try_easy_solve(test_puzzle)
            test_puzzle = try_hard_solve(test_puzzle)
            if is_solved(test_puzzle):
                return test_puzzle
    return puzzle

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
