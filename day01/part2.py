from typing import Optional

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
    for digit, value in DIGITS.items():
        if line.startswith(digit):
            return value
    return None


def solve_for_line(line: str) -> int:
    first_num = None
    second_num = None

    for i in range(len(line)):
        digit: Optional[int]
        if line[i].isnumeric():
            digit = int(line[i])
        else:
            digit = get_digit(line[i:])
        if digit is not None:
            if first_num is None:
                first_num = digit
                second_num = digit
            else:
                second_num = digit
    assert first_num is not None
    assert second_num is not None
    return first_num * 10 + second_num


def part2(lines: list[str]) -> int:
    result = 0
    for line in lines:
        result += solve_for_line(line)
    return result
