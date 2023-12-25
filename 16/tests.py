#!/usr/bin/env python3

import foo
import bar
import unittest

td1 = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""


class TestAll(unittest.TestCase):
    # def test_one(self):
    # score = bar.main(data=td1)
    # self.assertEqual(score, 46)

    def test_dots_only(self):
        score = bar.main(data="...\n...")
        self.assertEqual(score, 3)

    def test_entered(self):
        p = bar.Position(1, 1, ".")
        self.assertEqual(p.seen, False)
        p.see()
        self.assertEqual(p.seen, True)
        self.assertEqual([a for a in p.entered.values()], [False, False, False, False])
        p.enter("w")
        self.assertEqual(p.entered.get("w"), True)
