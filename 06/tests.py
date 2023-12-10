#!/usr/bin/env python3

import unittest
import foo

test_doc = """Time:      7  15   30
Distance:  9  40  200"""


class TestAll(unittest.TestCase):
    def test_parser(self):
        self.assertEqual(foo.parser(document=test_doc), ([7, 15, 30], [9, 40, 200]))

    def test_winners(self):
        self.assertEqual(foo.winners(duration=7, record=9), [2, 3, 4, 5])

    def test_winners_(self):
        self.assertEqual(foo.winners(duration=15, record=40), list(range(4, 12)))

    def test_winners__(self):
        self.assertEqual(foo.winners(duration=30, record=200), list(range(11, 20)))

    def test_main_part_1(self):
        self.assertEqual(foo.main_part_1(document=test_doc), 288)

    def test_main_part_2(self):
        self.assertEqual(foo.main_part_2(document=test_doc), 71503)
