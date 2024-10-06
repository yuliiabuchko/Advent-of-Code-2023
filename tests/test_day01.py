import unittest

from day01.parser import parser
from day01.part1 import part1
from day01.part2 import part2


class TestDay01(unittest.TestCase):

    def test_part_1(self) -> None:
        test_file = "input/day01/part1.txt"
        input_lines = parser(test_file)
        self.assertEqual(142, part1(input_lines))

    def test_part_2(self) -> None:
        test_file = "input/day01/part2.txt"
        input_lines = parser(test_file)
        self.assertEqual(281, part2(input_lines))
