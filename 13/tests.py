import foo
import unittest

td1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


class TestAll(unittest.TestCase):
    def test_get_data(self):
        self.assertEqual(foo.get_data(fname="td1.txt"), td1)

    def test_foo(self):
        m = foo.Mirrors(data=td1)
        self.assertEqual(m.h_mirrors, [0, 4])
        # print(m.h_mirrors, m.h_score, m.v_mirrors, m.v_score)
        self.assertEqual(m.total_score, 405)

    def test_debug(self):
        m = foo.Mirrors(data=td1)
        m.debug()

    def test_part_1(self):
        data = foo.get_data(fname="data.txt")
        m = foo.Mirrors(data=data)
        # m.debug()
        # print(m.total_score)
        self.assertEqual(m.total_score, 34821)
