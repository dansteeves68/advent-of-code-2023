#!/usr/bin/env python3


def test_for_mirror(mirror: int, pattern: list) -> bool:
    l = 0
    r = 1
    while 0 <= mirror - l < mirror + r < len(pattern):
        # print(mirror, l, r, pattern[mirror - l], pattern[mirror + r])
        if pattern[mirror - l] == pattern[mirror + r]:
            l += 1
            r += 1
        else:
            return False
    return True


def test_pattern(pattern: list):
    # Test for horizontal mirrors by walking the rows
    for i in range(0, len(pattern) - 1):
        # note this assumes there are no series of four identical rows
        if pattern[i] == pattern[i + 1]:
            if test_for_mirror(mirror=i, pattern=pattern):
                return i + 1
            try:
                if pattern[i] == pattern[i + 2]:
                    print("DANGER")
            except:
                pass
    return 0


class Mirrors:
    def __init__(self, data):
        self.data = data
        self.patterns = [a.split("\n") for a in self.data.split("\n\n")]
        self.h_mirrors = []
        self.v_mirrors = []

        for pattern in self.patterns:
            self.h_mirrors.append(test_pattern(pattern=pattern))
            # Rotate pattern to test vertical
            pattern_ = [
                [pattern[y][x] for y in range(0, len(pattern))]
                for x in range(0, len(pattern[0]))
            ]
            # print(pattern_)
            self.v_mirrors.append(test_pattern(pattern=pattern_))

        self.h_score = sum(self.h_mirrors) * 100
        self.v_score = sum(self.v_mirrors)
        self.total_score = self.h_score + self.v_score

    def __repr__(self):
        return repr(self.h_mirrors)

    def debug(self):
        for i, pattern in enumerate(self.patterns):
            print("### Pattern \n")
            for line in pattern:
                print(line)
            print(
                "\n",
                "H: ",
                self.h_mirrors[i],
                "\nV: ",
                self.v_mirrors[i],
            )


def get_data(fname: str) -> str:
    with open(fname, "r") as f:
        return f.read().strip()


def main(fname):
    data = get_data(fname=fname)
    m = Mirrors(data=data)
    return m.total_score


if __name__ == "__main__":
    print("Result: ", main(fname="data.txt"))
