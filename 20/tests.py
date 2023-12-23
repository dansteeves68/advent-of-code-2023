#!/usr/bin/env python3

import foo
import unittest

td1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""

td2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"""


class TestAll(unittest.TestCase):
    # @unittest.skip("to see output of second test")
    def test_td1(self):
        c = foo.Configuration(data=td1)
        ff = [a for a in c.modules.values()]
        ff = [a.on for a in ff if a.flipflop == True]
        self.assertEqual(ff, [False, False, False])
        self.assertEqual(c.score(), (8000, 4000, 32000000))

    def test_td2(self):
        c = foo.Configuration(data=td2)
        self.assertEqual(c.score(), (4250, 2750, 11687500))

    def test_part_1(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        c = foo.Configuration(data=data)
        self.assertEqual(c.score(), (17860, 51075, 912199500))
