from typing import Optional

from day03.part1 import add_dots_to_input


def part2(engine: list[list[str]]) -> int:
    n = len(engine)
    m = len(engine[0])

    engine = add_dots_to_input(engine)
    i = 1

    gears = {}

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


def surrounded_gear(engine: list[list[str]], i: int, j_start: int, j_end: int) -> Optional[tuple[int, int]]:
    if engine[i][j_start - 1] == '*':
        return i, j_start - 1
    if engine[i][j_end] == '*':
        return i, j_end
    for x in range(j_start - 1, j_end + 1):
        if engine[i - 1][x] == '*':
            return i - 1, x
        if engine[i + 1][x] == '*':
            return i + 1, x
    return None
