"""Module provides solution for part 2"""


from typing import Optional

from day01.part1 import updated_values

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_digit(line: str) -> Optional[int]:
    """Return integer digit if line starts with string representation"""
    for digit, value in DIGITS.items():
        if line.startswith(digit):
            return value
    return None


def solve_for_line(line: str) -> int:
    """Process single input line"""
    first_num = None
    last_num = None

    for i, char in enumerate(line):
        digit: Optional[int]
        if char.isnumeric():
            digit = int(char)
        else:
            digit = get_digit(line[i:])
        if digit is not None:
            first_num, last_num = updated_values(digit, first_num)
    assert first_num is not None
    assert last_num is not None
    return first_num * 10 + last_num


def part2(lines: list[str]) -> int:
    """Solve part 2"""
    return sum(solve_for_line(line) for line in lines)
