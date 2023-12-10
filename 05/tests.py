#!/usr/bin/env python3

import foo
import unittest

test_doc = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class Test(unittest.TestCase):
    def test_main(self):
        self.assertEqual(foo.main(fname="test_data.txt"), 46)

    def test_doc(self):
        self.assertEqual(foo.get_document(fname="test_data.txt"), test_doc)

    def test_is_seed(self):
        self.assertEqual(foo.is_seed(val=15, seeds=[(79, 14), (55, 13)]), False)
        self.assertEqual(foo.is_seed(val=78, seeds=[(79, 14), (55, 13)]), False)
        self.assertEqual(foo.is_seed(val=93, seeds=[(79, 14), (55, 13)]), False)
        self.assertEqual(foo.is_seed(val=80, seeds=[(79, 14), (55, 13)]), True)
        self.assertEqual(foo.is_seed(val=79, seeds=[(79, 14), (55, 13)]), True)
        self.assertEqual(foo.is_seed(val=92, seeds=[(79, 14), (55, 13)]), True)

    def test_parser(self):
        self.assertEqual(
            foo.parser(document=test_doc),
            (
                [(79, 14), (55, 13)],
                [
                    [[50, 98, 2], [52, 50, 48]],
                    [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
                    [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]],
                    [[88, 18, 7], [18, 25, 70]],
                    [[45, 77, 23], [81, 45, 19], [68, 64, 13]],
                    [[0, 69, 1], [1, 0, 69]],
                    [[60, 56, 37], [56, 93, 4]],
                ],
            ),
        )
