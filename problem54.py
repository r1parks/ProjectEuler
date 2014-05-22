#!/usr/bin/env python

import fileinput

cardRank = " a23456789TJQKA"

def cardVal(card):
    return cardRank.find(card[0])

def createHand(cards):
    hand = []
    for card in cards:
        hand.append((card[0], card[1]))
    return sorted(hand, key=cardVal)[::-1]

def createHands(input_line):
    cards = input_line.split()
    h1 = createHand(cards[:5])
    h2 = createHand(cards[5:])
    return h1, h2

def highCardScore(hand):
    h_score = 0
    for card in hand:
        h_score *= 15
        h_score += cardVal(card)
    return h_score

def pairScore(hand):
    for c in range(len(hand)-1):
        if hand[c][0] == hand[c+1][0]:
            return (15**5) * cardVal(hand[c]) + highCardScore(hand[:c] + hand[c+2:])
    return 0

def twoPairScore(hand):
    for c in range(len(hand)-3):
        if hand[c][0] == hand[c+1][0]:
            smallerPairScore = pairScore(hand[:c] + hand[c+2:])
            if smallerPairScore == 0:
                return 0
            return (15**6) * cardVal(hand[c]) + smallerPairScore
    return 0

def threeKindScore(hand):
    for c in range(len(hand)-2):
        if hand[c][0] == hand[c+1][0] == hand[c+2][0]:
            return (15**7) * cardVal(hand[c])
    return 0

def straightScore(hand):
    for c in range(len(hand)-1):
        if cardVal(hand[c]) != cardVal(hand[c+1]) + 1:
            if hand[0][0] == 'A':
                return straightScore(hand[1:] + [('a', hand[0][1])])
            else:
                return 0
    return (15 ** 8) * cardVal(hand[0])

def flushScore(hand):
    suit = hand[0][1]
    for card in hand:
        if card[1] != suit:
            return 0
    return (15 ** 9) * cardVal(hand[0])

def fullBoatScore(hand):
    tkScore = threeKindScore(hand[:3]) * (15 ** 8)
    if tkScore == 0:
        return 0
    pScore = pairScore(hand[3:])
    if pScore == 0:
        return 0
    return tkScore + pScore

def fourKindScore(hand):
    for c in range(len(hand)-3):
        if hand[c][0] == hand[c+1][0] == hand[c+2][0] == hand[c+3][0]:
            return (15 ** 11) * cardVal(hand[c]) + highCardScore(hand[:c] + hand[c+4:])
    return 0

def straightFlushScore(hand):
    if flushScore(hand) == 0:
        return 0
    return straightScore(hand) * (15 ** 8)

def score(hand):
    max_score = 0
    max_score = max(max_score, highCardScore(hand))
    max_score = max(max_score, pairScore(hand))
    max_score = max(max_score, twoPairScore(hand))
    max_score = max(max_score, threeKindScore(hand))
    max_score = max(max_score, straightScore(hand))
    max_score = max(max_score, flushScore(hand))
    max_score = max(max_score, fullBoatScore(hand))
    max_score = max(max_score, fourKindScore(hand))
    max_score = max(max_score, straightFlushScore(hand))
    return max_score

def doesP1Win(h1, h2):
    return 1 if score(h1) > score(h2) else 0

if __name__ == '__main__':
    p1_wins = 0
    for line in fileinput.input():
        h1, h2 = createHands(line)
        p1_wins += doesP1Win(h1, h2)
    print "{}".format(p1_wins)
