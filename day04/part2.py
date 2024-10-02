from day04.parser import Card


def part2(cards: list[Card]) -> int:
    card_copies = {}
    for card in cards:
        card_wins = 0
        for possessed in card.possessed_numbers:
            if possessed in card.winning_numbers:
                card_wins += 1
        if card.id not in card_copies:
            card_copies[card.id] = 0
        card_copies[card.id] += 1
        for x in range(card.id + 1, card.id + card_wins + 1):
            if x not in card_copies:
                card_copies[x] = 0
            card_copies[x] += card_copies[card.id]

    return sum(card_copies.values())
