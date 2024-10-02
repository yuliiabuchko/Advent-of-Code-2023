class Card:
    def __init__(self, num: int, winning_numbers: list[int], possessed_numbers: list[int]):
        self.id = num
        self.winning_numbers = winning_numbers
        self.possessed_numbers = possessed_numbers


def parser(path: str) -> list[Card]:
    res = []
    with open(path, 'r') as file:
        for line in file.readlines():
            card_with_num, numbers = line.strip().split(":")
            winning, possessed = numbers.split("|")
            card_num = int(card_with_num.split()[1])
            winning_numbers = list(map(int, winning.strip().split()))
            possessed_numbers = list(map(int, possessed.strip().split()))
            res.append(Card(card_num, winning_numbers, possessed_numbers))
    return res
