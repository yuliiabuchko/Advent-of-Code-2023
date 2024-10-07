"""Module provides solution for part 2"""

from typing import Optional

from day03.part1 import add_dots_to_input

GEAR = '*'


def part2(engine: list[list[str]]) -> int:
    """Solve part 2"""
    n = len(engine)
    m = len(engine[0])

    engine = add_dots_to_input(engine)
    i = 1

    gears: dict[tuple[int, int], list[str]] = {}

    while i <= n:
        j = 1
        curr_num = ''
        start = None
        while j <= m + 1:
            if engine[i][j].isnumeric():
                curr_num += engine[i][j]
                if start is None:
                    start = j
            elif curr_num:
                assert start is not None
                gear = surrounded_gear(engine, i, start, j)
                if gear is not None:
                    if gear not in gears:
                        gears[gear] = []
                    gears[gear].append(curr_num)
                curr_num = ''
                start = None
            j += 1
        i += 1

    total = 0
    for gear, values in gears.items():
        if len(values) == 2:
            total += int(values[0]) * int(values[1])
    return total


def surrounded_gear(engine: list[list[str]], i: int, j_start: int, j_end: int)\
        -> Optional[tuple[int, int]]:
    """Check if number is surrounded by gear, if so - return its coordinates"""
    if engine[i][j_start - 1] == GEAR:
        return i, j_start - 1
    if engine[i][j_end] == GEAR:
        return i, j_end
    for x in range(j_start - 1, j_end + 1):
        if engine[i - 1][x] == GEAR:
            return i - 1, x
        if engine[i + 1][x] == GEAR:
            return i + 1, x
    return None
