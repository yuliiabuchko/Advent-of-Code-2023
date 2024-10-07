"""Module to test solution"""
import os
import unittest
from pathlib import Path

from day02.parser import parser
from day02.part1 import part1
from day02.part2 import part2

THIS_DIR = Path(__file__).parent


class TestDay02(unittest.TestCase):
    """Test day 02 solution"""

    def setUp(self) -> None:
        test_file = os.path.join(THIS_DIR, "input/day02/input.txt")
        self.input_lines = parser(test_file)

    def test_part_1(self) -> None:
        """Test part 1 solution"""
        self.assertEqual(8, part1(self.input_lines))

    def test_part_2(self) -> None:
        """Test part 2 solution"""
        self.assertEqual(2286, part2(self.input_lines))
