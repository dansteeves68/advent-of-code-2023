#!/usr/bin/env python3

import foo
import unittest

td1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


class TestAll(unittest.TestCase):
    def test_td1(self):
        result = foo.main_part_1(data=td1, min=7, max=27)
        self.assertEqual(result, 2)

    def test_td1(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        result = foo.main_part_1(data=data, min=200000000000000, max=400000000000000)
        self.assertEqual(result, 2)
