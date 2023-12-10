#!/usr/bin/env python3

import foo
import unittest

td1 = """.....
.S-7.
.|.|.
.L-J.
....."""

td2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

td3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""


class TestAll(unittest.TestCase):
    def test_map_1(self):
        p = foo.Pipes(doc=td1)
        p.map()
        p.route()
        self.assertEqual(p.len(), 4)

    def test_map_2(self):
        p = foo.Pipes(doc=td2)
        p.map()
        p.route()
        self.assertEqual(p.len(), 8)

    def test_main_part_1(self):
        self.assertEqual(foo.main_part_1(), 7030)

    def test_is_interior(self):
        p = foo.Pipes(doc=td3)
        p.map()
        p.route()
        # self.assertEqual(p.is_interior(point=(6, 2)), True)
        self.assertEqual(p.is_interior(point=(3, 4)), False)
