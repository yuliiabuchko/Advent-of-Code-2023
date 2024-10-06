import importlib


def format_input_path(day: int) -> str:
    return f"input/day{format(day, '02d')}/input.txt"


def show_result(day: int) -> None:
    print(f"DAY {format(day, '02d')}")
    path = format_input_path(day)
    parser = importlib.import_module(f'day{format(day, "02d")}.parser')
    parsed_input = parser.parser(path)

    part1 = importlib.import_module(f'day{format(day, "02d")}.part1')
    print(f"Part 1: {part1.part1(parsed_input)}")

    part2 = importlib.import_module(f'day{format(day, "02d")}.part2')
    print(f"Part 2: {part2.part2(parsed_input)}")

    print()


DAYS = 5
if __name__ == '__main__':
    for i in range(DAYS):
        show_result(i + 1)
