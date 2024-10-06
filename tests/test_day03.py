import unittest

from day03.parser import parser
from day03.part1 import part1
from day03.part2 import part2


class TestDay03(unittest.TestCase):
    def setUp(self) -> None:
        test_file = "input/day03/input.txt"
        self.engine = parser(test_file)

    def test_part_1(self) -> None:
        self.assertEqual(4361, part1(self.engine))

    def test_part_2(self) -> None:
        self.assertEqual(467835, part2(self.engine))
