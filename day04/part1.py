"""Module provides solution for part 1"""

from day04.parser import Card


def part1(cards: list[Card]) -> int:
    """Solve part 1"""
    total = 0
    for card in cards:
        card_wins = calculate_card_wins(card)
        if card_wins != 0:
            total += 2 ** (card_wins - 1)
    return total


def calculate_card_wins(card: Card) -> int:
    """Calculate wins for card"""
    card_wins = 0
    for possessed in card.possessed_numbers:
        if possessed in card.winning_numbers:
            card_wins += 1
    return card_wins
