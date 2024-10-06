import unittest

from day02.parser import parser
from day02.part1 import part1
from day02.part2 import part2


class TestDay02(unittest.TestCase):
    def setUp(self) -> None:
        test_file = "input/day02/input.txt"
        self.input_lines = parser(test_file)

    def test_part_1(self) -> None:
        self.assertEqual(8, part1(self.input_lines))

    def test_part_2(self) -> None:
        self.assertEqual(2286, part2(self.input_lines))
