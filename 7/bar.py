#!/usr/bin/env python3

from collections import Counter


def sortable_cards(cards):
    lookup = {
        "A": "a",
        "K": "b",
        "Q": "c",
        "J": "n",
        "T": "e",
        "9": "f",
        "8": "g",
        "7": "h",
        "6": "i",
        "5": "j",
        "4": "k",
        "3": "l",
        "2": "m",
    }
    sortable_cards = list(cards)
    sortable_cards = [lookup.get(a) for a in sortable_cards]
    return "".join(sortable_cards)


def simple_score(cards):
    counts = Counter(cards)
    if max(counts.values()) == 5:
        score = "0"
    elif max(counts.values()) == 4:
        score = "1"
    elif 3 in counts.values() and 2 in counts.values():
        score = "2"
    elif 3 in counts.values() and not 2 in counts.values():
        score = "3"
    elif len([a for a in counts.values() if a == 2]) == 2:
        score = "4"
    elif 2 in counts.values():
        score = "5"
    elif max(counts.values()) == 1:
        score = "6"
    return score


def joker_score(cards):
    counts = Counter(cards)
    jokers = counts.get("n", 0)
    if jokers == 0:
        joker_cards = cards
    elif jokers == 5:
        joker_cards = cards
    else:
        del counts["n"]
        max_key = max(counts, key=counts.get)
        joker_cards = cards.replace("n", max_key)
    score = simple_score(cards=joker_cards)
    print(cards, joker_cards, score)
    return score


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.sortable_cards = sortable_cards(cards=self.cards)
        self.simple_score = simple_score(cards=self.sortable_cards)
        self.joker_score = joker_score(cards=self.sortable_cards)

    def __repr__(self):
        return repr(
            (
                self.cards,
                self.bid,
                self.sortable_cards,
                self.simple_score,
                self.joker_score,
            )
        )


def parser(doc):
    result = []
    lines = doc.split("\n")
    for line in lines:
        c, b = line.split()
        hand = Hand(cards=c, bid=int(b))
        result.append(hand)
    return result


def main_part_1(doc):
    hands = parser(doc)
    hands = sorted(hands, key=lambda hand: hand.sortable_cards, reverse=True)
    hands = sorted(hands, key=lambda hand: hand.simple_score, reverse=True)
    winnings = 0
    i = 1
    for hand in hands:
        winnings += hand.bid * i
        i += 1
    return winnings


def main_part_2(doc):
    hands = parser(doc)
    hands = sorted(hands, key=lambda hand: hand.sortable_cards, reverse=True)
    hands = sorted(hands, key=lambda hand: hand.joker_score, reverse=True)
    print(hands)
    winnings = 0
    i = 1
    for hand in hands:
        winnings += hand.bid * i
        i += 1
    return winnings


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        document = f.read().strip()
    print(document)
    winnings = main_part_2(doc=document)
    print("Result Part 2: ", winnings)
