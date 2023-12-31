import foo
import unittest

td1 = r""".|...\....
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
    def test_part_1_sample(self):
        self.assertEqual(foo.main_part_1(data=td1), 46)

    def test_part_1(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        self.assertEqual(foo.main_part_1(data=data), 7210)

    def test_part_2_sample(self):
        self.assertEqual(foo.main_part_2(data=td1), 51)
