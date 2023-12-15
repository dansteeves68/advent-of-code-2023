#!/usr/bin/env python3


def get_document(fname):
    with open(fname, "r") as f:
        document = f.read().strip()
    return document


def is_seed(val, seeds):
    for seed in seeds:
        if seed[0] <= val < seed[0] + seed[1]:
            return True
        else:
            return False


def parser(document):
    l = [int(a) for a in document.split("\n")[0].split(":")[1].strip().split()]
    seeds = []
    for i in range(0, len(l), 2):
        seeds.append((l[i], l[i + 1]))
    maps = document.split("\n\n")[1:]
    maps = [a.split(":")[1].strip().split("\n") for a in maps]
    maps = [[[int(c) for c in a.split()] for a in b] for b in maps]
    return seeds, maps

def transform(val, maps)
:
def transformer(val, maps):
    seed = val
    for map in reversed(maps):
        seed = transform(seed, map)
    return seed


def main(fname, max=50):
    document = get_document(fname)
    seeds, maps = parser(document=document)
    for i in range(0, max):
        if is_seed(transformer(i, maps)):
            return i
    return False
