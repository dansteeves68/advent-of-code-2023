#!/usr/bin/env python3

import unittest
import foo

test_doc = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


class TestAll(unittest.TestCase):
    def test_symbols(self):
        print(foo.find_symbols(test_doc))

    def test_part_numbers(self):
        print(foo.find_part_numbers(test_doc))

    def test_adjacent(self):
        print(foo.calc_adjacent((2, (2, 4), "35")))

    def test_main(self):
        print(foo.main(test_doc))


class TestPart2(unittest.TestCase):
    def test_stars(self):
        print(foo.find_stars(test_doc))

    def test_main_2(self):
        print(foo.main_part_2(test_doc))
