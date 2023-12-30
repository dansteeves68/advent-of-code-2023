#!/usr/bin/env python3

import foo
import unittest

td1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


class TestAll(unittest.TestCase):
    def test_sample_1(self):
        self.assertEqual(foo.main_part_1(data=td1, steps=6), 16)

    def test_part_1(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        self.assertEqual(foo.main_part_1(data=data, steps=64), 3542)
