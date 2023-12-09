#!/usr/bin/env python3

import foo
import unittest

test_doc = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_instructions = "RL"

test_network = {
    "AAA": ("BBB", "CCC"),
    "BBB": ("DDD", "EEE"),
    "CCC": ("ZZZ", "GGG"),
    "DDD": ("DDD", "DDD"),
    "EEE": ("EEE", "EEE"),
    "GGG": ("GGG", "GGG"),
    "ZZZ": ("ZZZ", "ZZZ"),
}

test_doc_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""


class TestAll(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(foo.get_data("test_data.txt"), test_doc)

    def test_parser(self):
        self.assertEqual(foo.parser(test_doc)[0], "RL")
        self.assertEqual(foo.parser(test_doc)[1], test_network)

    def test_walker(self):
        self.assertEqual(
            foo.walker(
                network=test_network,
                instructions=test_instructions,
                start="AAA",
                target="ZZZ",
            ),
            2,
        )

    def test_walker_2(self):
        instructions, network = foo.parser(test_doc_2)
        self.assertEqual(
            foo.walker(
                network=network,
                instructions=instructions,
                start="AAA",
                target="ZZZ",
            ),
            6,
        )


test_doc_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


class TestPart2(unittest.TestCase):
    def test_part_2(self):
        self.assertEqual(foo.main_part_2(test_doc_3), 6)
