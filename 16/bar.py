#!/usr/bin/env python3

direction = {
    "n": (0, -1),
    "s": (0, 1),
    "e": (1, 0),
    "w": (-1, 0),
}


class Position:
    def __init__(self, y, x, char):
        self.y = y
        self.x = x
        self.char = char
        self.entered = {"n": False, "s": False, "e": False, "w": False}
        self.seen = False

    def exit_v(self, current_v):
        if self.char == ".":
            return current_v

    def see(self):
        self.seen = True

    def enter(self, dir):
        self.entered[dir] = True


class Beam:
    def __init__(self, y, x, v):
        self.y = y
        self.x = x
        self.v = v

    def move(self, next_position):
        exit_v = self.exit_v(self)
        pass

    def run(self, positions) -> list:
        new_beams = []
        while self.v:
            next_y = self.y + direction.get(self.v)[0]
            next_x = self.x + direction.get(self.v)[1]
            next_p = positions.get((next_y, next_x), None)
            if not next_p:
                self.v = None
                break
            self.move(next_p)

        return new_beams


def main(data):
    grid = data.split("\n")
    len_y = len(grid)
    len_x = len(grid[0])
    p = {}
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            p[y, x] = Position(y, x, char)

    print(p)
    beam = Beam(0, 0, "e")
    p[0, 0].see()

    new_beams = [beam]
    while new_beams:
        b = new_beams.pop(0)
        new_beams.extend(b.run(positions=p))

    return 0
