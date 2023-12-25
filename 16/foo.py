#!/usr/bin/env python3


class Beam:
    def __init__(self, y, x, yv, xv):
        self.y = y
        self.x = x
        self.yv = yv
        self.xv = xv
        self.position = (self.y, self.x)
        self.velocity = (self.yv, self.xv)
        self.next_position = (self.y + self.yv, self.x + self.xv)
        self.path = []

    def update(self):
        """update position, next_positoin, path after move"""
        self.position = (self.y, self.x)
        self.path.append(self.position)
        self.velocity = (self.yv, self.xv)
        self.next_position = (self.y + self.yv, self.x + self.xv)

    def end(self):
        """set velocities to zero,
        beam is done"""
        self.yv = 0
        self.xv = 0
        self.update()

    def advance(self, char: str):
        """move beam to next position
        change velocity if needed"""
        self.y += self.yv
        self.x += self.xv
        self.update()

        # turn north
        if (self.velocity, char) in [((0, 1), "/"), ((0, -1), "\\")]:
            self.yv = -1
            self.xv = 0
        # turn south
        if (self.velocity, char) in [((0, 1), "\\"), ((0, -1), "/")]:
            self.yv = 1
            self.xv = 0
        # turn east
        if (self.velocity, char) in [((-1, 0), "/"), ((1, 0), "\\")]:
            self.yv = 0
            self.xv = 1
        # turn west
        if (self.velocity, char) in [((-1, 0), "\\"), ((1, 0), "/")]:
            self.yv = 0
            self.xv = -1


class Contraption:
    def __init__(self, data):
        self.data = data
        self.grid = self.data.split("\n")
        self.len_y = len(self.grid)
        self.len_x = len(self.grid[0])
        self.score = 0
        self.beams = [Beam(y=0, x=-1, yv=0, xv=1)]
        for beam in self.beams:
            step(beam, self)
        self.energized = []
        for beam in self.beams:
            print(beam.path)
            self.energized.extend(beam.path)
            self.energized = list(set(self.energized))

    def lookup(self, y: int, x: int) -> str:
        return self.grid[y][x]


def step(beam, contraption):
    print("step")
    next_y, next_x = beam.next_position
    # stop if next postion is out of bounds
    if (
        next_y < 0
        or next_x < 0
        or next_y >= contraption.len_y
        or next_x > contraption.len_x
    ):
        beam.end()
        return False
    while contraption.lookup(y=next_y, x=next_x) in [".", "/", "\\"]:
        print("advance")
        beam.advance(char=contraption.lookup(y=next_y, x=next_x))
        next_y, next_x = beam.next_position
