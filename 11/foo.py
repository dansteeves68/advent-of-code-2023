#!/usr/bin/env python3


class Universe:
    def __init__(self, data, multiplier=1):
        self.data = data
        self.multiplier = multiplier
        self.y = 0
        self.x = 0
        self.empty_y = []
        self.empty_x = []
        self.galaxies = []
        self.distances = []
        self.sum_of_shortest_paths = 0

    def parse(self):
        for y, line in enumerate(self.data.split("\n")):
            self.y = y
            for x, char in enumerate(line):
                self.x = x
                if char == "#":
                    self.galaxies.append((y, x))
        pop_y = [a[0] for a in self.galaxies]
        self.empty_y = [a for a in range(0, self.y + 1) if a not in pop_y]
        pop_x = [a[1] for a in self.galaxies]
        self.empty_x = [a for a in range(0, self.x + 1) if a not in pop_x]
        for i, this_galaxy in enumerate(self.galaxies[:-1]):
            for other_galaxy in self.galaxies[i + 1 :]:
                y_travel = range(
                    min(this_galaxy[0], other_galaxy[0]),
                    max(this_galaxy[0], other_galaxy[0]),
                )
                x_travel = range(
                    min(this_galaxy[1], other_galaxy[1]),
                    max(this_galaxy[1], other_galaxy[1]),
                )
                y_travel_ = [a for a in y_travel if a in self.empty_y]
                x_travel_ = [a for a in x_travel if a in self.empty_x]
                y_travel = len(y_travel) + len(y_travel_) * self.multiplier
                self.sum_of_shortest_paths += y_travel
                x_travel = len(x_travel) + len(x_travel_) * self.multiplier
                self.sum_of_shortest_paths += x_travel


def get_data(fname):
    with open(fname, "r") as f:
        return f.read().strip()


def main_part_1(fname, multiplier=1):
    data = get_data(fname=fname)
    u = Universe(data=data, multiplier=multiplier)
    u.parse()
    return u.sum_of_shortest_paths


if __name__ == "__main__":
    print("Result Part 1: ", main_part_1(fname="data.txt"))
    print("Result Part 2: ", main_part_1(fname="data.txt", multiplier=999999))
