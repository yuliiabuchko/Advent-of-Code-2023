"""Module provides solution for part 2"""

from typing import Optional

from day03.part1 import solve

GEAR = '*'


def part2(engine: list[list[str]]) -> int:
    """Solve part 2"""
    gears = solve(engine, {}, is_surrounded_by_gear, add_to_gears)

    total = 0
    for values in gears.values():
        if len(values) == 2:
            total += int(values[0]) * int(values[1])
    return total


def is_surrounded_by_gear(engine: list[list[str]], i: int, start: int, j: int) \
        -> tuple[bool, Optional[tuple[int, int]]]:
    """Check if number is surrounded by gear, if so - return its coordinates"""
    gear = surrounded_gear(engine, i, start, j)
    return gear is not None, gear


def add_to_gears(curr_num: str, gear: tuple[int, int],
                 gears: dict[tuple[int, int], list[str]]) \
        -> dict[tuple[int, int], list[str]]:
    """Add `curr_num` to gears dict"""
    if gear not in gears:
        gears[gear] = []
    gears[gear].append(curr_num)
    return gears


def surrounded_gear(engine: list[list[str]], i: int, j_start: int, j_end: int) \
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
