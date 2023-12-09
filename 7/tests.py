#!/usr/bin/env python3

import bar
import foo
import unittest

test_doc = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


class TestAll(unittest.TestCase):
    def test_parser(self):
        print(foo.parser(doc=test_doc))

    def test_main_part_1(self):
        self.assertEqual(foo.main_part_1(doc=test_doc), 6440)


class TestJokers(unittest.TestCase):
    def test_main_part_2(self):
        self.assertEqual(bar.main_part_2(doc=test_doc), 5905)
