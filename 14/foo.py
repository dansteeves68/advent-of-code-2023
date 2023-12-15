#!/usr/bin/env python3


def tilted(rocks: str) -> str:
    result = ""
    rounds = ""
    dots = ""
    for rock in rocks:
        if rock == "#":
            result += rounds
            result += dots
            result += "#"
            rounds = ""
            dots = ""
        elif rock == "O":
            rounds += "O"
        elif rock == ".":
            dots += "."
    result += rounds
    result += dots
    return result


def score(rocks: str) -> int:
    score = 0
    length = len(rocks)
    for i, char in enumerate(rocks):
        if char == "O":
            score += length - i
    return score


class Rocks:
    def __init__(self, data):
        self.data = data

        rows = self.data.split("\n")
        # create a N-S list for each column
        self.columns = [
            [rows[y][x] for y in range(0, len(rows))] for x in range(0, len(rows[0]))
        ]
        self.columns = ["".join(a) for a in self.columns]
        # slide rocks on each column
        self.columns = [tilted(a) for a in self.columns]
        # score columns
        self.scores = [score(a) for a in self.columns]

        self.total_load = sum(self.scores)

    def __repr__(self):
        return repr(self.total_load)


def get_data(fname: str) -> str:
    with open(fname, "r") as f:
        return f.read().strip()


def main(fname):
    data = get_data(fname=fname)
    r = Rocks(data=data)
    return r.total_load


if __name__ == "__main__":
    print("Result: ", main(fname="data.txt"))
