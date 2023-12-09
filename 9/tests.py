#!/usr/bin/env python3

import foo
import unittest

test_doc = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


class TestPart1(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(
            foo.parser(document=test_doc),
            [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]],
        )

    def test_f1(self):
        self.assertEqual(foo.forecast(values=[0, 3, 6, 9, 12, 15]), 18)

    def test_f2(self):
        self.assertEqual(foo.forecast(values=[1, 3, 6, 10, 15, 21]), 28)

    def test_f3(self):
        self.assertEqual(foo.forecast(values=[10, 13, 16, 21, 30, 45]), 68)

    def test_f4(self):
        self.assertEqual(foo.forecast(values=[3, 3, 3]), 3)

    def test_main_part_1(self):
        self.assertEqual(foo.main_part_1(fname="test_data.txt"), 114)
