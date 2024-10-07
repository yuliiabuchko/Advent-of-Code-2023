"""Module provides solution for part 1"""
from typing import Optional


def solve_for_line(line: str) -> int:
    """Process single input line"""
    first_num = None
    last_num = None

    for char in line:
        if char.isnumeric():
            first_num, last_num = updated_values(int(char), first_num)
    assert first_num is not None
    assert last_num is not None
    return first_num * 10 + last_num


def updated_values(digit: int, first_num: Optional[int]) -> tuple[int, int]:
    """Update first and last number"""
    if first_num is None:
        first_num = digit
        second_num = digit
    else:
        second_num = digit
    return first_num, second_num


def part1(lines: list[str]) -> int:
    """Solve part 1"""
    return sum(solve_for_line(line) for line in lines)
