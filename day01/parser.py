"""Module parses and processes input"""


def parser(input_path: str) -> list[str]:
    """Function reads and parses input"""
    with open(input_path, 'r', encoding='utf-8') as input_file:
        return input_file.readlines()
