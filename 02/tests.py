#!/usr/bin/env python3

import unittest
import foo

g1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
g2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
g3 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
g4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
g5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"

bag = {"red": 12, "green": 13, "blue": 14}

class TestAll(unittest.TestCase):

    def test_simple(self):
        print(foo.game_parser("Game 1: 1 green, 2 red, 6 blue; 4 red, 1 green, 3 blue; 7 blue, 5 green; 6 blue, 2 red, 1 green"))

    def test_g1(self):
        game = foo.game_parser(g1)
        self.assertTrue(foo.game_tester(bag, game.get("samples")))

    def test_g2(self):
        game = foo.game_parser(g2)
        self.assertTrue(foo.game_tester(bag, game.get("samples")))

    def test_g3(self):
        game = foo.game_parser(g3)
        self.assertFalse(foo.game_tester(bag, game.get("samples")))

    def test_g4(self):
        game = foo.game_parser(g4)
        self.assertFalse(foo.game_tester(bag, game.get("samples")))

    def test_g5(self):
        game = foo.game_parser(g5)
        self.assertTrue(foo.game_tester(bag, game.get("samples")))

class TestMin(unittest.TestCase):

    def test_g1(self):
        game = foo.game_parser(g1)
        self.assertEqual(foo.game_minimizer(samples=game.get("samples")), {"red": 4, "green": 2, "blue": 6})

    def test_g2(self):
        game = foo.game_parser(g2)
        self.assertEqual(foo.game_minimizer(samples=game.get("samples")), {"red": 1, "green": 3, "blue": 4})

    def test_g3(self):
        game = foo.game_parser(g3)
        self.assertEqual(foo.game_minimizer(samples=game.get("samples")), {"red": 20, "green": 13, "blue": 6})

    def test_g4(self):
        game = foo.game_parser(g4)
        self.assertEqual(foo.game_minimizer(samples=game.get("samples")), {"red": 14, "green": 3, "blue": 15})

    def test_g5(self):
        game = foo.game_parser(g5)
        self.assertEqual(foo.game_minimizer(samples=game.get("samples")), {"red": 6, "green": 3, "blue": 2})

