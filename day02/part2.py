from day02.parser import Game


def part2(games: list[Game]) -> int:
    res = 0
    for game in games:
        max_red = max(entry.red for entry in game.entries)
        max_green = max(entry.green for entry in game.entries)
        max_blue = max(entry.blue for entry in game.entries)
        res += max_blue * max_red * max_green
    return res
