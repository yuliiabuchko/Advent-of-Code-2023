from typing import Optional

from day01.part1 import parser

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


def solve_for_line(line: str) -> int:
    first_num = None
    second_num = None

    for i in range(len(line)):
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
    return first_num * 10 + second_num


def part2(lines: list[str]) -> int:
    result = 0
    for line in lines:
        result += solve_for_line(line)
    return result


if __name__ == '__main__':
    input = parser("../input/day01/input.txt")
    print(part2(input))
