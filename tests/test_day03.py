"""Module to test solution"""
import os
import unittest
from pathlib import Path

from day03.parser import parser
from day03.part1 import part1
from day03.part2 import part2

THIS_DIR = Path(__file__).parent


class TestDay03(unittest.TestCase):
    """Test day 03 solution"""

    def setUp(self) -> None:
        test_file = os.path.join(THIS_DIR, "input/day03/input.txt")
        self.engine = parser(test_file)

    def test_part_1(self) -> None:
        """Test part 1 solution"""
        self.assertEqual(4361, part1(self.engine))

    def test_part_2(self) -> None:
        """Test part 2 solution"""
        self.assertEqual(467835, part2(self.engine))
