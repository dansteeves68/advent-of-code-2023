#!/usr/bin/env python3

import re


def find_symbols(document):
    symbols = []
    for a, line in enumerate(document.split("\n")):
        for b, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbols.append((a, b))
    return symbols


def find_stars(document):
    stars = []
    for a, line in enumerate(document.split("\n")):
        for b, char in enumerate(line):
            if char == "*":
                stars.append((a, b))
    return stars


def find_part_numbers(document):
    regex = re.compile("[0-9]+")
    part_numbers = []
    for a, line in enumerate(document.split("\n")):
        b = 0
        while b < len(line):
            match = regex.search(line, b)
            if match:
                part_numbers.append((a, match.span(), match.group()))
                b = match.span()[1] + 1
            else:
                break
    return part_numbers


def calc_adjacent(part_number):
    adjacents = []
    a, span = part_number[0], part_number[1]
    span = range(span[0] - 1, span[1] + 1)
    for b in span:
        adjacents.extend([(a - 1, b), (a + 1, b)])
    adjacents.extend([(a, span[0]), (a, span[-1])])
    return adjacents


def main(document):
    result = []
    symbols = find_symbols(document)
    symbols = set(symbols)
    part_numbers = find_part_numbers(document)
    for part_number in part_numbers:
        adjacents = calc_adjacent(part_number)
        intersection = symbols & set(adjacents)
        if len(intersection) > 0:
            result.append(int(part_number[2]))
    return sum(result)


def main_part_2(document):
    map = {}
    result = []
    stars = find_stars(document)
    for star in stars:
        map[star] = []
    part_numbers = find_part_numbers(document)
    for part_number in part_numbers:
        adjacents = calc_adjacent(part_number)
        intersections = list(set(stars) & set(adjacents))
        for i in intersections:
            map[i].append(part_number)
    for p in map.keys():
        if len(map.get(p)) == 2:
            result.append([int(a[2]) for a in map.get(p)])
    result = [a[0] * a[1] for a in result]
    return sum(result)


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        document = f.read()
    result = main(document)
    print("Result Part 1: ", result)
    result = main_part_2(document)
    print("Result Part 2: ", result)
