#!/usr/bin/env python3

import math
import numpy


class Pipes:
    def __init__(self, doc):
        self.doc = doc
        self.grid = {}
        self.s = ()
        self.loop = []

    def __repr__(self):
        return repr((self.s, self.loop))

    def len(self):
        return math.ceil(len(self.loop) / 2)

    def map(self):
        for y, line in enumerate(self.doc.split("\n")):
            for x, char in enumerate(line):
                self.grid[(y, x)] = char
                if char == "S":
                    self.s = (y, x)

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


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        doc = f.read().strip()
    p = Pipes(doc=doc)
    p.map()
    p.route()
    print("Result Part 1: ", p.len())
