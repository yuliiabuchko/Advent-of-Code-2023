"""Module provides solution for part 2"""
from day06.parser import Game
from day06.part1 import find_lowest_time_to_hold, calculate_possibilities_on_lowest_time


def fix_kerning(games: list[Game]) -> Game:
    """Fix input kerning"""
    time_str = ''.join(str(game.time) for game in games)
    distance_str = ''.join(str(game.record_distance) for game in games)
    return Game(int(time_str), int(distance_str))


def part2(games: list[Game]) -> int:
    """Solve part 2"""
    game = fix_kerning(games)
    lowest_time = find_lowest_time_to_hold(game)
    return calculate_possibilities_on_lowest_time(lowest_time, game)
