#!/usr/bin/env python

import problem54 as poker

def test_card_val():
    test_vals = {(('a', 'X'),) : 1,
                 (('2', 'X'),) : 2,
                 (('3', 'X'),) : 3,
                 (('4', 'X'),) : 4,
                 (('5', 'X'),) : 5,
                 (('6', 'X'),) : 6,
                 (('7', 'X'),) : 7,
                 (('8', 'X'),) : 8,
                 (('9', 'X'),) : 9,
                 (('T', 'X'),) : 10,
                 (('J', 'X'),) : 11,
                 (('Q', 'X'),) : 12,
                 (('K', 'X'),) : 13,
                 (('A', 'X'),) : 14}
    run_test(test_vals, poker.cardVal)

def test_create_hand():
    test_vals = {(("8C", "TS", "KC", "9H", "4S"),) : [('K', 'C'), ('T', 'S'), ('9', 'H'), ('8', 'C'), ('4', 'S')],
                 (("7D", "2S", "5D", "3S", "AC"),) : [('A', 'C'), ('7', 'D'), ('5', 'D'), ('3', 'S'), ('2', 'S')]}
    run_test(test_vals, poker.createHand)

def test_create_hands():
    test_vals = {("8C TS KC 9H 4S 7D 2S 5D 3S AC",) : ([('K', 'C'), ('T', 'S'), ('9', 'H'), ('8', 'C'), ('4', 'S')], [('A', 'C'), ('7', 'D'), ('5', 'D'), ('3', 'S'), ('2', 'S')])}
    run_test(test_vals, poker.createHands)

def test_high_card():
    test_vals = {'8C TS KC 9H 4S 7D 2S 5D 3S AC' : False,
                 '5C AD 5D AC 9C 7C 5H 8D TD KS' : True,
                 '3H 7H 6S KC JS QH TD JC 2D 8S' : True,
                 'TH 8H 5C QS TC 9H 4D JC KS JS' : False,
                 '7C 5H KC QH JD AS KH 4C AD 4S' : False,
                 '5H KS 9C 7D 9H 8D 3S 5D 5C AH' : False,
                 '6H 4H 5C 3H 2H 3S QH 5S 6S AS' : False,
                 'TD 8C 4H 7C TC KC 4C 3H 7S KS' : False,
                 'AH 9H 8H 7H 6H AC 9C 8C 7C 5C' : True,
                 'AH 9H 8C 7H 2H AC 9C 8H 7C 6C' : False }
    run_test2(test_vals, poker.highCardScore)

def test_pair():
    test_vals = {'8C 8S KC 9H 4S 2D 2S 2D 3S AC' : True,
                 '5C AD 5D AC 9C 7C 5H 8D TD KS' : True,
                 '3H 7H 6S KC 3S QH TD JC 2D 8S' : True,
                 'TH 8H 5C QS TC KH 4D JC KS JS' : False,
                 '7C 5H KC QH JD AS KH 4C AD 4S' : False,
                 '5H KS 9C 7D 3H 8D 3S 5D 5C AH' : False,
                 '6H 4H 5C 2H 2H AS AH 5S 6S AS' : False,
                 '6H 4H 5C 2H 2H 6H 4H 5C 2H 2H' : False,
                 '6H 4H 5C 3H 2H 3S QH 5S 6S AS' : False,
                 'TD 8C 4H 7C TC KC 4C 3H 7S KS' : False,
                 'AH AH 4H 5H 6H AC AC 3C 5C 6C' : True,
                 '6H 6H 2C 8H 9H 6C 6C 8H 9C 3C' : False }
    run_test2(test_vals, poker.pairScore)

def test_two_pair():
    test_vals = {'8C 8S 6C 6H AS 8D 8S 6D 6S 2C' : True,
                 '8C 8S 6C 6H 2S 8D 8S 6D 6S 2C' : False,
                 '5C AD 5D AC 9C AC AH 2D 2D KS' : True,
                 '3H 3H 2S 2C 7S 3H 3D JC 2D 8S' : True,
                 'TH TH QC QS AC AH AD KC KS JS' : False,
                 '7C 7H KC KH JD 7S 7H KC KD JS' : False }
    run_test2(test_vals, poker.twoPairScore)

def test_three_kind():
    run_test2(test_vals, poker)

def run_test2(vals, func):
    for card_string in vals.viewkeys():
        h1, h2 = poker.createHands(card_string)
        test_val = func(h1) > func(h2)
        if test_val != vals[card_string]:
            print "ERROR: {}({}) = {}\n\tExpected: {}".format(func.func_name, card_string, test_val, vals[card_string])

def run_test(vals, func):
    for args in vals.viewkeys():
        ret_val = func(*args)
        if ret_val != vals[args]:
            print "ERROR: {}({}) = {}\n\tExpected: {}".format(func.func_name, args, ret_val, vals[args])

if __name__ == '__main__':
    test_card_val()
    test_create_hand()
    test_create_hands()
    test_high_card()
    test_pair()
    test_two_pair()
