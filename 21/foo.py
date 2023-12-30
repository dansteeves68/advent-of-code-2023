#!/usr/bin/env python3

import networkx as nx


def main_part_1(data, steps):
    graph = nx.Graph()
    for y, line in enumerate(data.split("\n")):
        for x, char in enumerate(line):
            if char != "#":
                graph.add_node((y, x))
                if (y - 1, x) in graph.nodes:
                    graph.add_edge((y, x), (y - 1, x))
                if (y, x - 1) in graph.nodes:
                    graph.add_edge((y, x), (y, x - 1))
                if char == "S":
                    start = (y, x)

    sources = [start]
    for i in range(0, steps):
        next = []
        for source in sources:
            successors = nx.bfs_successors(graph, source, depth_limit=1)
            sources = []
            for s in successors:
                next.extend(s[1])
        sources = list(set(next))

    print(sources)
    return len(sources)
