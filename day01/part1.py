def solve_for_line(line: str) -> int:
    first_num = None
    second_num = None

    for i in range(len(line)):
        if line[i].isnumeric():
            digit = int(line[i])
            if first_num is None:
                first_num = digit
                second_num = digit
            else:
                second_num = digit
    assert first_num is not None
    assert second_num is not None
    return first_num * 10 + second_num


def part1(lines: list[str]) -> int:
    result = 0
    for line in lines:
        result += solve_for_line(line)
    return result
