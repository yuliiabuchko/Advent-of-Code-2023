"""Module provides solution for part 1"""
from typing import Callable, Any

DOT = '.'

MeetConditionFunction = Callable[[list[list[str]], int, int, int], tuple[bool, Any]]
ProcessIfMeetsConditionFunction = Callable[[str, Any, Any], Any]


def part1(engine: list[list[str]]) -> Any:
    """Solve part 1"""
    return solve(engine, 0, is_surrounded_by_symbol, add_to_total)


def solve(engine: list[list[str]], total: Any,
          meets_condition_func: MeetConditionFunction,
          func: ProcessIfMeetsConditionFunction) -> Any:
    """Process engine values with `func` once `meets_condition_func` condition is met"""
    n = len(engine)
    m = len(engine[0])
    engine = add_dots_to_input(engine)
    i = 1
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
                meets_condition, out = meets_condition_func(engine, i, start, j)
                if meets_condition:
                    total = func(curr_num, out, total)
                curr_num = ''
                start = None
            j += 1
        i += 1
    return total


def add_to_total(curr_num: str, _: Any, total: int) -> int:
    """Add `curr_num` to total"""
    total += int(curr_num)
    return total


def is_surrounded_by_symbol(engine: list[list[str]], i: int, j_start: int, j_end: int)\
        -> tuple[bool, None]:
    """Check if number is surrounded by any symbol"""
    if engine[i][j_start - 1] != DOT or engine[i][j_end] != DOT:
        return True, None
    for x in range(j_start - 1, j_end + 1):
        if engine[i - 1][x] != DOT or engine[i + 1][x] != DOT:
            return True, None
    return False, None


def add_dots_to_input(engine: list[list[str]]) -> list[list[str]]:
    """Add dots around the input grid"""
    res = []
    columns_num = len(engine[0])
    res.append([DOT for _ in range(columns_num)])
    for line in engine:
        res.append([DOT] + line + [DOT])
    res.append([DOT for _ in range(columns_num)])
    return res
