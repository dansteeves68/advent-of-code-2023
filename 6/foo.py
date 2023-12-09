#!/usr/bin/env python3
from functools import reduce
from operator import mul


def parser(document):
    durations, records = (
        [int(a) for a in document.split("\n")[0].split(":")[1].split()],
        [int(a) for a in document.split("\n")[1].split(":")[1].split()],
    )
    return durations, records


def winners(duration, record):
    winners = []
    for hold in range(0, duration + 1):
        if (duration - hold) * hold > record:
            winners.append(hold)
    return winners


def main_part_1(document):
    durations, records = parser(document=document)
    results = []
    for i in range(0, len(durations)):
        results.append(winners(duration=durations[i], record=records[i]))
    results = [len(a) for a in results]
    return reduce(mul, results, 1)


def main_part_2(document):
    durations, records = parser(document=document)
    duration = int("".join([str(a) for a in durations]))
    record = int("".join([str(a) for a in records]))
    results = winners(duration=duration, record=record)
    return len(results)


if __name__ == "__main__":
    with open("data.txt", "r") as f:
        document = f.read()
    result = main_part_1(document)
    print("Result Part 1: ", result)
    result = main_part_2(document)
    print("Result Part 2: ", result)
