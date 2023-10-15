# simulating the frequencies of "marriage" and "divorces" when shuffling a deck of cards
# a marriage means at least one king-queen pair are directly next to each other
# a divorce means that at least one king-queen pair are only one card apart

import numpy as np
import matplotlib.pyplot as plt
import random

# simplified cards, Kings, Queens, and Neither
cards = 4 * ["K"] + 4 * ["Q"] + 44 * ["N"]

n_divorces = 0
n_marriages = 0
n_either = 0

N_SHUFFLES = 1_000_000

for _ in range(N_SHUFFLES):
    marriage = False
    divorce = False

    random.shuffle(cards)
    king_locs = [i for i, card in enumerate(cards) if card == 'K']
    queen_locs = [i for i, card in enumerate(cards) if card == 'Q']
    for k in king_locs:
        for q in queen_locs:
            if (k + 1 == q) or (k - 1 == q):
                marriage = True
                break
    for k in king_locs:
        for q in queen_locs:
            if (k + 2 == q) or (k - 2 == q):
                divorce = True
                break
    if marriage:
        n_marriages += 1
    if divorce:
        n_divorces += 1
    if marriage or divorce:
        n_either += 1

print(f"number of marriages: {n_marriages}, percentage: {n_marriages / N_SHUFFLES}")
print(f"number of divorces: {n_divorces}, percentage: {n_divorces / N_SHUFFLES}")
print(f"number of either: {n_either}, percentage: {n_either / N_SHUFFLES}")