"""Module provides solution for part 1"""
from day06.parser import Game


def calculate_distance_for_time(time: int, game: Game) -> int:
    """Calculate distance for holding time"""
    return time * (game.time - time)


def binsearch_lowest_time(start: int, end: int, game: Game) -> int:
    """Execute binsearch recursively to find the lowest time to hold"""
    if start == end:
        return start
    mid = (start + end) // 2
    mid_value = calculate_distance_for_time(mid, game)

    if mid_value > game.record_distance:
        return binsearch_lowest_time(start, mid, game)
    return binsearch_lowest_time(mid + 1, end, game)


def find_lowest_time_to_hold(game: Game) -> int:
    """
    Calculate the lowest time needed to win the game
    y = t * (T - t) > D
    """
    start = 0
    end = game.time // 2
    return binsearch_lowest_time(start, end, game)


def calculate_possibilities_on_lowest_time(lowest_time: int, game: Game) -> int:
    """Count all possible winning ranges. Equal to all numbers in range [t, T - t]"""
    return game.time - 2 * lowest_time + 1


def part1(games: list[Game]) -> int:
    """Solve part 1"""
    all_possibilities = 1
    for game in games:
        lowest_time = find_lowest_time_to_hold(game)
        possibilities = calculate_possibilities_on_lowest_time(lowest_time, game)
        all_possibilities *= possibilities
    return all_possibilities
