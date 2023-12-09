#!/usr/bin/env python3

from binarytree import Node


def walker(network, instructions, start, target):
    map = {"L": 0, "R": 1}
    steps = 0
    current_node = start
    while current_node != target:
        step = steps % len(instructions)
        new_node = network.get(current_node)[map.get(instructions[step])]
        current_node = new_node
        steps += 1
    return steps


def parser(data):
    lines = data.split("\n")
    instructions = lines[0]
    network = {}
    for line in lines[2:]:
        id = line.split()[0]
        left = line.split()[2][1:4]
        right = line.split()[3][0:3]
        network[id] = (left, right)
    return instructions, network


def get_data(fname):
    with open(fname, "r") as f:
        data = f.read().strip()
    return data


def walker_2(network, instructions, starts):
    map = {"L": 0, "R": 1}
    steps = 0
    current_nodes = starts
    new_nodes = ["" for a in current_nodes]
    while len([a for a in current_nodes if a.endswith("Z")]) < len(starts):
        step = steps % len(instructions)
        for i, cn in enumerate(current_nodes):
            new_nodes[i] = network.get(cn)[map.get(instructions[step])]
        current_nodes = new_nodes
        steps += 1
    return steps


def main_part_2(data):
    i, n = parser(data)
    results = []
    starts = [a for a in n.keys() if a.endswith("A")]
    result = walker_2(network=n, instructions=i, starts=starts)
    return result


if __name__ == "__main__":
    data = get_data("data.txt")
    instructions, network = parser(data)
    result = walker(network, instructions, start="AAA", target="ZZZ")
    print("Result Part 1: ", result)
    result = main_part_2(data=data)
    print("Result Part 2: ", result)
