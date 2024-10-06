from day05.parser import Almanac, GameMap


def process_seed(seed: int, almanac: Almanac) -> int:
    source = "seed"
    curr_number = seed
    while True:
        game_map = find_destination(source, almanac)
        curr_number = process_map(curr_number, game_map)
        if game_map.destination == "location":
            return curr_number
        source = game_map.destination


def process_map(number: int, game_map: GameMap) -> int:
    for entry in game_map.entries:
        if entry.source_start <= number < entry.source_end:
            return entry.destination_start + number - entry.source_start
    return number


def find_destination(source: str, almanac: Almanac) -> GameMap:
    for game_map in almanac.maps:
        if game_map.source == source:
            return game_map


def part1(almanac: Almanac) -> int:
    return min(process_seed(seed, almanac) for seed in almanac.seeds)
