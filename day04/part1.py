from day04.parser import Card


def part1(cards: list[Card]) -> int:
    total = 0
    for card in cards:
        card_wins = 0
        for possessed in card.possessed_numbers:
            if possessed in card.winning_numbers:
                card_wins += 1
        if card_wins != 0:
            total += 2 ** (card_wins - 1)
    return total
