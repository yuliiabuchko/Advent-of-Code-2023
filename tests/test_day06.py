"""Module to test solution"""
import os
import unittest
from pathlib import Path

from day06.parser import parser
from day06.part1 import part1
from day06.part2 import part2

THIS_DIR = Path(__file__).parent


class TestDay06(unittest.TestCase):
    """Test day 06 solution"""

    def setUp(self) -> None:
        test_file = os.path.join(THIS_DIR, "input/day06/input.txt")
        self.games = parser(test_file)

    def test_part_1(self) -> None:
        """Test part 1 solution"""
        self.assertEqual(288, part1(self.games))

    def test_part_2(self) -> None:
        """Test part 2 solution"""
        self.assertEqual(71503, part2(self.games))
