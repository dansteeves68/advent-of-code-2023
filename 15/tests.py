#!/usr/bin/env python3

import foo
import unittest

td1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""


class TestAll(unittest.TestCase):
    def test_hash(self):
        self.assertEqual(foo.hash("HASH"), 52)

    def test_init(self):
        self.assertEqual(foo.init(data=td1), 1320)

    def test_part_1(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        self.assertEqual(foo.init(data=data), 509784)

    def test_main(self):
        b = foo.Boxes()
        for i in td1.split(","):
            b.process(i)
        self.assertEqual(
            b.boxes[:4],
            [
                [("rn", "1"), ("cm", "2")],
                [],
                [],
                [("ot", "7"), ("ab", "5"), ("pc", "6")],
            ],
        )
        self.assertEqual(b.score(), 145)

    def test_part_2(self):
        b = foo.Boxes()
        with open("data.txt", "r") as f:
            data = f.read().strip()
        for i in data.split(","):
            b.process(i)
        self.assertEqual(b.score(), 230197)
