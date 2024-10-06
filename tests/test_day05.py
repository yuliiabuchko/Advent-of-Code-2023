import unittest

from day05.parser import parser
from day05.part1 import part1
from day05.part2 import part2


class TestDay05(unittest.TestCase):
    def setUp(self) -> None:
        test_file = "input/day05/input.txt"
        self.almanac = parser(test_file)

    def test_part_1(self) -> None:
        self.assertEqual(part1(self.almanac), 35)

    def test_part_2(self) -> None:
        self.assertEqual(part2(self.almanac), 46)
