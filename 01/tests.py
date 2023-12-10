#!/usr/bin/env python3

import unittest
import foo

class TestAll(unittest.TestCase):

	def test_simple(self):
		self.assertEqual(foo.parser("pqr3stu8vwx"), 38)

	def test_spelling(self):
		self.assertEqual(foo.parser("abcone2threexyz"), 13)