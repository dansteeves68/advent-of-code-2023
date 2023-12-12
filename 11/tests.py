#!/usr/bin/env python3

import foo
import unittest


td1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


class TestAll(unittest.TestCase):
    def test_main_part_1(self):
        self.assertEqual(foo.main_part_1(fname="td1.txt"), 374)

    def test_get_data(self):
        self.assertEqual(foo.get_data(fname="td1.txt"), td1)

    def test_galaxies(self):
        u = foo.Universe(data=td1)
        u.parse()
        self.assertEqual(
            u.galaxies,
            [(0, 3), (1, 7), (2, 0), (4, 6), (5, 1), (6, 9), (8, 7), (9, 0), (9, 4)],
        )
        self.assertEqual(u.empty_y, [3, 7])
        self.assertEqual(u.empty_x, [2, 5, 8])
