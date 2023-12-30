#!/usr/bin/env python3

import networkx as nx


def main_part_1(data):
    graph = nx.DiGraph()
    for y, line in enumerate(data.split("\n")):
        for x, char in enumerate(line):
            current = (y, x)
            north = (y - 1, x)
            west = (y, x - 1)
            if char != "#":
                graph.add_node((y, x), char=char)
                if north in graph.nodes:
                    north_char = graph.nodes[north].get("char")
                    if north_char in [".", "v"] and char != "^":
                        graph.add_edge(north, current)
                    if north_char != ">" and char in [".", "^"]:
                        graph.add_edge(current, north)
                if west in graph.nodes:
                    west_char = graph.nodes[west].get("char")
                    if west_char in [".", ">"] and char != "<":
                        graph.add_edge(west, current)
                    if north_char != ">" and char in [".", "<"]:
                        graph.add_edge(current, west)

    # print(graph.nodes[(22, 21)].get("char"))

    source = list(graph.nodes)[0]
    target = list(graph.nodes)[-1]

    # print(source, target)

    results = []
    paths = nx.all_simple_paths(graph, source, target)
    for path in paths:
        results.append(len(path) - 1)

    return max(results)
