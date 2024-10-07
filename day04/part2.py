"""Module provides solution for part 2"""

from day04.parser import Card
from day04.part1 import calculate_card_wins


def part2(cards: list[Card]) -> int:
    """Solve part 2"""
    card_copies = {}
    for card in cards:
        card_wins = calculate_card_wins(card)
        if card.id not in card_copies:
            card_copies[card.id] = 0
        card_copies[card.id] += 1
        for x in range(card.id + 1, card.id + card_wins + 1):
            if x not in card_copies:
                card_copies[x] = 0
            card_copies[x] += card_copies[card.id]

    return sum(card_copies.values())
