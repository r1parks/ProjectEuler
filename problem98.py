#!/usr/bin/env python

from pe_tools import is_square
from collections import defaultdict

def word_key(word):
    return ''.join(sorted(word))

def find_palindromes(word):
    palindromes = defaultdict(list)
    for word in words:
        k = word_key(word)
        palindromes[k].append(word)
    return filter(lambda n: len(n) > 1, palindromes.values())

def square_gen():
    i = 1
    while True:
        yield i * i
        i += 1

def int_key(i):
    k = ''.join(sorted(str(i)))
    while len(k) < len(str(i)):
        k = '0' + k
    return k

def find_square_palindromes():
    square_palindromes = [defaultdict(list) for _ in range(10)]
    squares = square_gen()
    for square in squares:
        if square >= 10**9:
            break
        k = int_key(square)
        square_palindromes[len(str(square))][k].append(square)
    keys_to_delete = []
    for i in range(len(square_palindromes)):
        for key in square_palindromes[i]:
            if len(square_palindromes[i][key]) < 2:
                keys_to_delete.append((i,key))
    assert len(set(keys_to_delete)) == len(keys_to_delete)
    for i, k in keys_to_delete:
        del square_palindromes[i][k]
    return square_palindromes
    
def longest(palindromes):
    return sorted(map(lambda n: len(n[0]), palindromes))[-1]

def get_input():
    with open("p098_words.txt", 'r') as f:
        w = map(lambda n: n[1:-1], f.read().split(','))
    return w

def pattern_match(word, number):
    num_key = str(number)
    for i in range(len(word)-1):
        try:
            if word[i] == word[i+1] or num_key[i] == num_key[i+1]:
                if not(word[i] == word[i+1] and num_key[i] == num_key[i+1]):
                    return False
        except:
            import pdb; pdb.set_trace()
            pass
    return True

def create_mapping(word, num):
    num = str(num)
    mapping = {}
    for i in range(len(word)):
        mapping[word[i]] = num[i]
    return mapping

def create_num(word, mapping):
    str_num = ''
    for c in word:
        str_num += mapping[c]
    return int(str_num)

def test_mapping(mapping, words, numbers):
    matches = set()
    for word in words:
        new_num = create_num(word, mapping)
        if new_num in numbers:
            matches.add(new_num)
    return matches

def match_words(palindrome, squares):
    matches = set()
    for word in palindrome:
        for square in squares:
            mapping = create_mapping(palindrome[0], squares[0])
            additional_matches = test_mapping(mapping, palindrome[1:], squares[1:])
            if len(additional_matches) >= 0:
                additional_matches.add(squares[0])
                matches.update(additional_matches)
    return matches

def find_match(palindrome, squares):
    matches = []
    for key in squares:
        if pattern_match(palindrome[0], key):
            word_matches = match_words(palindrome, squares[key])
            if len(word_matches) > 1:
                matches += word_matches
    return matches

if __name__ == '__main__':
    words = get_input()
    palindromes = find_palindromes(words)
    squares = find_square_palindromes()
    current_max = 0
    for palindrome in palindromes:
        match = find_match(palindrome, squares[len(palindrome[0])])
        if match:
            if max(match) > current_max:
                current_max = max(match)
    print current_max
