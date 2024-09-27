def parser(input_path: str) -> list[str]:
    with open(input_path, 'r') as input_file:
        return input_file.readlines()


def solve_for_line(line: str) -> int:
    first_num = None
    second_num = None

    for i in range(len(line)):
        if line[i].isnumeric():
            if first_num is None:
                first_num = line[i]
                second_num = line[i]
            else:
                second_num = line[i]
    return int(first_num) * 10 + int(second_num)


def part1(lines: list[str]) -> int:
    result = 0
    for line in lines:
        result += solve_for_line(line)
    return result


if __name__ == '__main__':
    input = parser("../input/day01/input.txt")
    print(part1(input))
