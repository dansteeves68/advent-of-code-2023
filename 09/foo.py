#!/usr/bin/env python3


def parser(document):
    data = []
    for line in document.split("\n"):
        data.append([int(a) for a in line.split()])
    return data


def forecast(values):
    diff = [values[i] - values[i - 1] for i in range(1, len(values))]
    if sum(diff) == 0:
        return values[-1]
    else:
        return values[-1] + forecast(values=diff)


def main_part_1(fname):
    with open(fname, "r") as f:
        document = f.read().strip()
    data = parser(document=document)
    result = 0
    for values in data:
        result += forecast(values=values)
    return result


def precast(values):
    diff = [values[i] - values[i - 1] for i in range(1, len(values))]
    if sum(diff) == 0:
        return values[0]
    else:
        return values[0] - precast(values=diff)


def main_part_2(fname):
    with open(fname, "r") as f:
        document = f.read().strip()
    data = parser(document=document)
    result = 0
    for values in data:
        result += precast(values=values)
    return result


if __name__ == "__main__":
    result = main_part_1(fname="data.txt")
    print("Result Part 1: ", result)
    result = main_part_2(fname="data.txt")
    print("Result Part 2: ", result)
