"""Module parses and processes input"""
import dataclasses


@dataclasses.dataclass
class Card:
    """Input card"""
    id: int
    winning_numbers: list[int]
    possessed_numbers: list[int]


def parser(path: str) -> list[Card]:
    """Function reads and parses input"""
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            card_with_num, numbers = line.strip().split(":")
            winning, possessed = numbers.split("|")
            card_num = int(card_with_num.split()[1])
            winning_numbers = list(map(int, winning.strip().split()))
            possessed_numbers = list(map(int, possessed.strip().split()))
            res.append(Card(card_num, winning_numbers, possessed_numbers))
    return res
