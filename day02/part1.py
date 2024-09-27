from day02.parser import Game, GameEntry


def is_game_entry_possible(game_entry: GameEntry) -> bool:
    return game_entry.red <= 12 and game_entry.green <= 13 and game_entry.blue <= 14


def is_game_possible(game: Game) -> bool:
    return all(is_game_entry_possible(game_entry) for game_entry in game.entries)


def part1(games: list[Game]) -> int:
    res = 0
    for game in games:
        if is_game_possible(game):
            res += game.id
    return res
