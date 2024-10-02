def parser(path: str) -> list[list[str]]:
    res = []
    with open(path, 'r') as file:
        for line in file.readlines():
            res.append(list(line.strip()))
    return res
