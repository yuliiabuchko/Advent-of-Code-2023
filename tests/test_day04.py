import unittest

from day04.parser import parser
from day04.part1 import part1
from day04.part2 import part2


class TestDay04(unittest.TestCase):
    def setUp(self) -> None:
        test_file = "input/day04/input.txt"
        self.cards = parser(test_file)

    def test_part_1(self) -> None:
        self.assertEqual(13, part1(self.cards))

    def test_part_2(self) -> None:
        self.assertEqual(30, part2(self.cards))
