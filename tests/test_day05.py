"""Module to test solution"""
import os
import unittest
from pathlib import Path

from day05.parser import parser
from day05.part1 import part1
from day05.part2 import part2

THIS_DIR = Path(__file__).parent


class TestDay05(unittest.TestCase):
    """Test day 05 solution"""

    def setUp(self) -> None:
        test_file = os.path.join(THIS_DIR, "input/day05/input.txt")
        self.almanac = parser(test_file)

    def test_part_1(self) -> None:
        """Test part 1 solution"""
        self.assertEqual(35, part1(self.almanac))

    def test_part_2(self) -> None:
        """Test part 2 solution"""
        self.assertEqual(46, part2(self.almanac))
