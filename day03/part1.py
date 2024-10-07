"""Module provides solution for part 1"""


DOT = '.'


def part1(engine: list[list[str]]) -> int:
    """Solve part 1"""
    total = 0

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
                if is_surrounded_by_symbol(engine, i, start, j):
                    total += int(curr_num)
                curr_num = ''
                start = None
            j += 1
        i += 1
    return total


def is_surrounded_by_symbol(engine: list[list[str]], i: int, j_start: int, j_end: int) -> bool:
    """Check if number is surrounded by any symbol"""
    if engine[i][j_start - 1] != DOT or engine[i][j_end] != DOT:
        return True
    for x in range(j_start - 1, j_end + 1):
        if engine[i - 1][x] != DOT or engine[i + 1][x] != DOT:
            return True
    return False


def add_dots_to_input(engine: list[list[str]]) -> list[list[str]]:
    """Add dots around the input grid"""
    res = []
    columns_num = len(engine[0])
    res.append([DOT for _ in range(columns_num)])
    for line in engine:
        res.append([DOT] + line + [DOT])
    res.append([DOT for _ in range(columns_num)])
    return res
