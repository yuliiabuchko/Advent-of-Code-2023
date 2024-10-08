"""Module provides solution for part 1"""
from day05.parser import Almanac, GameMap


def process_seed(seed: int, almanac: Almanac) -> int:
    """Process seed into almanac maps"""
    source = "seed"
    curr_number = seed
    while True:
        game_map = find_destination(source, almanac)
        curr_number = process_map(curr_number, game_map)
        if game_map.destination == "location":
            return curr_number
        source = game_map.destination


def process_map(number: int, game_map: GameMap) -> int:
    """Calculate destination for number for game map"""
    for entry in game_map.entries:
        if entry.contains_number(number):
            return entry.calculate_destination_for_number(number)
    return number


def find_destination(source: str, almanac: Almanac) -> GameMap:
    """Find next map in almanac"""
    for game_map in almanac.maps:
        if game_map.source == source:
            return game_map
    raise ValueError


def part1(almanac: Almanac) -> int:
    """Solve part 1"""
    return min(process_seed(seed, almanac) for seed in almanac.seeds)
