"""Module provides solution for part 1"""

from day02.parser import Game, GameEntry


def is_game_entry_possible(game_entry: GameEntry) -> bool:
    """Check if game entry is possible"""
    return game_entry.red <= 12 and game_entry.green <= 13 and game_entry.blue <= 14


def is_game_possible(game: Game) -> bool:
    """Check if all entries of the game are possible"""
    return all(is_game_entry_possible(game_entry) for game_entry in game.entries)


def part1(games: list[Game]) -> int:
    """Solve part 1"""
    res = 0
    for game in games:
        if is_game_possible(game):
            res += game.id
    return res
