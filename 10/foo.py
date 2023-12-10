#!/usr/bin/env python3

import math
import numpy


class Pipes:
    def __init__(self, doc):
        self.doc = doc
        self.grid = {}
        self.s = ()
        self.loop = []
        self.y = None
        self.x = None

    def __repr__(self):
        return repr((self.s, self.loop))

    def len(self):
        return math.ceil(len(self.loop) / 2)

    def is_interior(self, point):
        edges = self.loop
        edges.append(self.s)
        y, x = point
        n = [(a, x) for a in range(0, y)]
        s = [(a, x) for a in range(y + 1, self.y)]
        e = [(y, a) for a in range(x + 1, self.x)]
        w = [(y, a) for a in range(0, x)]
        crosses = []
        for c in [n, s, e, w]:
            c = [a for a in c if a in edges]
            crosses.append(c)
        if min([len(a) % 2 for a in crosses]) == 0:
            return False
        else:
            return True

    def count_interior(self):
        edges = self.loop
        edges.append(self.s)
        interior = 0
        for y in range(0, self.y):
            for x in range(0, self.x):
                print(y, " of ", self.y, " and ", x, " of ", self.x)
                if (y, x) not in edges:
                    if self.is_interior((y, x)):
                        interior += 1
        return interior

    def map(self):
        for y, line in enumerate(self.doc.split("\n")):
            for x, char in enumerate(line):
                self.grid[(y, x)] = char
                if char == "S":
                    self.s = (y, x)
                self.y, self.x = y + 1, x + 1

    north = (-1, 0)
    south = (1, 0)
    east = (0, 1)
    west = (0, -1)
    ends = {
        "S": [north, south, east, west],
        "|": [north, south],
        "-": [east, west],
        "L": [north, east],
        "J": [north, west],
        "7": [south, west],
        "F": [south, east],
        ".": [],
    }

    def route(self):
        current = self.get_next(None, self.s)
        last = self.s
        loop = []
        next = None
        while next != self.s:
            loop.append(current)
            next = self.get_next(last, current)
            last = current
            current = next
        self.loop = loop

    def get_next(self, last, current):
        symbol = self.grid[current]
        options = [tuple(numpy.add(current, a)) for a in self.ends.get(symbol)]
        for next in options:
            if next == last:
                continue
            next_symbol = self.grid[next]
            if current in [
                tuple(numpy.add(next, a)) for a in self.ends.get(next_symbol)
            ]:
                return next


def main_part_1():
    with open("data.txt", "r") as f:
        doc = f.read().strip()
    p = Pipes(doc=doc)
    p.map()
    p.route()
    print("Result Part 1: ", p.len())
    print("Result Part 2: ", p.count_interior())
    return p.len()


if __name__ == "__main__":
    main_part_1()
