"""Module to test solution"""
import os
import unittest
from pathlib import Path

from day01.parser import parser
from day01.part1 import part1
from day01.part2 import part2

THIS_DIR = Path(__file__).parent


class TestDay01(unittest.TestCase):
    """Test day 01 solution"""

    def test_part_1(self) -> None:
        """Test part 1 solution"""
        test_file = os.path.join(THIS_DIR, "input/day01/part1.txt")
        input_lines = parser(test_file)
        self.assertEqual(142, part1(input_lines))

    def test_part_2(self) -> None:
        """Test part 2 solution"""
        test_file = os.path.join(THIS_DIR, "input/day01/part2.txt")
        input_lines = parser(test_file)
        self.assertEqual(281, part2(input_lines))
