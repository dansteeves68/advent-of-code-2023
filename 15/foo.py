#!/usr/bin/env python3


def hash(input: str) -> int:
    value = 0
    for char in input:
        value += ord(char)
        value = value * 17
        value = value % 256
    return value


def init(data: str) -> int:
    total = 0
    for step in data.split(","):
        total += hash(input=step)
    return total
