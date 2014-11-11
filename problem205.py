#!/usr/bin/env python

def dice_combinations(n, sides):
    combinations = [0] * (n * sides + 1)
    if n == 1:
        for i in range(1, sides+1):
            combinations[i] = 1
        return combinations
    prev_combinations = dice_combinations(n-1, sides)
    for i in range(n, n*sides+1):
        s = sum(prev_combinations[max(i-sides, 0):i])
        combinations[i] = s
    return combinations

def dice_odds(n, sides):
    combinations = dice_combinations(n, sides)
    probabiliites = [0.0] * len(combinations)
    total = float(sum(combinations))
    for i in range(len(probabiliites)):
        probabiliites[i] = combinations[i] / total
    return probabiliites

if __name__ == '__main__':
    d_6_6_odds = dice_odds(6, 6)
    d_4_9_odds = dice_odds(9, 4)
    total = 0.0
    for i in range(len(d_4_9_odds)):
        total += d_4_9_odds[i] * sum(d_6_6_odds[:i])
    print round(total, 7)
