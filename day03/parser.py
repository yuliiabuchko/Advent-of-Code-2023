"""Module parses and processes input"""


def parser(path: str) -> list[list[str]]:
    """Function reads and parses input"""
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            res.append(list(line.strip()))
    return res
