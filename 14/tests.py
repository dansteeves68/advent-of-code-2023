import foo
import unittest

td1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


class TestAll(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(foo.get_data(fname="td1.txt"), td1)

    def test_tilted(self):
        self.assertEqual(foo.tilted("O.O)"), "OO.")
        self.assertEqual(foo.tilted("#.O"), "#O.")
        self.assertEqual(foo.tilted("#.OO#O.#..O"), "#OO.#O.#O..")

    def test_tilted(self):
        self.assertEqual(foo.score("OO."), 5)

    def test_td1(self):
        r = foo.Rocks(data=td1)
        # print(r.columns)
        self.assertEqual(r.total_load, 136)

    def test_part_1(self):
        data = foo.get_data(fname="data.txt")
        r = foo.Rocks(data=data)
        self.assertEqual(r.total_load, 108840)
