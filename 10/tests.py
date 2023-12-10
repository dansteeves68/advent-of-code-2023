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


class TestAll(unittest.TestCase):
    def test_map_1(self):
        p = foo.Pipes(doc=td1)
        p.map()
        p.route()
        print(p)
        self.assertEqual(p.len(), 4)

    def test_map_2(self):
        p = foo.Pipes(doc=td2)
        p.map()
        p.route()
        print(p)
        self.assertEqual(p.len(), 8)
