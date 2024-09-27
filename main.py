from typing import Callable, Any


def solve_day_01(path: str) -> tuple[int, int]:
    from day01.parser import parser
    from day01.part1 import part1
    from day01.part2 import part2

    lines = parser(path)
    return part1(lines), part2(lines)


def solve_day_02(path: str) -> tuple[int, int]:
    from day02.parser import parser
    from day02.part1 import part1
    from day02.part2 import part2

    games = parser(path)
    return part1(games), part2(games)


def format_input_path(day: int) -> str:
    return f"input/day{format(day, '02d')}/input.txt"


def show_result(day: int, solver: Callable[[str], tuple[Any, Any]]) -> None:
    print(f"DAY {format(day, '02d')}")
    part1, part2 = solver(format_input_path(day))
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
    print()


if __name__ == '__main__':
    show_result(1, solve_day_01)
    show_result(2, solve_day_02)
