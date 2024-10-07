"""Module provides solution for part 2"""
from day05.parser import Almanac, GameRange, GameMap
from day05.part1 import find_destination


def process_game_map(ranges: list[GameRange], game_map: GameMap) -> list[GameRange]:
    """Calculate possible destination ranges for map"""
    res = []
    for _range in ranges:
        range_covered = []
        for entry in game_map.entries:
            if entry.source.start <= _range.start <= _range.end <= entry.source.end:
                res.append(GameRange(entry.calculate_destination_for_number(_range.start),
                                     entry.calculate_destination_for_number(_range.end)))
                range_covered.append(GameRange(_range.start, _range.end))
                continue
            if _range.start <= entry.source.start <= entry.source.end <= _range.end:
                res.append(GameRange(entry.calculate_destination_for_number(entry.source.start),
                                     entry.calculate_destination_for_number(entry.source.end)))
                range_covered.append(GameRange(entry.source.start, entry.source.end))
                continue
            if entry.source.start <= _range.start <= entry.source.end:
                res.append(GameRange(entry.calculate_destination_for_number(_range.start),
                                     entry.calculate_destination_for_number(entry.source.end)))
                range_covered.append(GameRange(_range.start, entry.source.end))
                continue
            if entry.source.start <= _range.end <= entry.source.end:
                res.append(GameRange(entry.calculate_destination_for_number(entry.source.start),
                                     entry.calculate_destination_for_number(_range.end)))
                range_covered.append(GameRange(entry.source.start, _range.end))
                continue
        range_covered = sorted(range_covered, key=lambda x: x.start)
        res.extend(get_uncovered(_range, range_covered))

    return res


def get_uncovered(_range: GameRange, range_covered: list[GameRange]) -> list[GameRange]:
    """Return all uncovered ranges"""
    if not range_covered:
        return [_range]
    res = []
    s = _range.start
    for range_cover in range_covered:
        if s == range_cover.start:
            s = range_cover.end
            continue
        res.append(GameRange(s, range_cover.start))
        s = range_cover.end
    if s != _range.end:
        res.append(GameRange(s, _range.end))
    return res


def process_seed_range(seed_ranges: list[GameRange], almanac: Almanac) -> list[GameRange]:
    """Process seed ranges into almanac maps"""
    source = "seed"
    ranges_starts = seed_ranges
    while True:
        game_map = find_destination(source, almanac)
        ranges_starts = process_game_map(ranges_starts, game_map)
        if game_map.destination == "location":
            return ranges_starts
        source = game_map.destination


def part2(almanac: Almanac) -> int:
    """Solve part 2"""
    input_seeds_ranges = []
    i = 0
    while i < len(almanac.seeds):
        input_seeds_ranges.append(GameRange(almanac.seeds[i],
                                            almanac.seeds[i] + almanac.seeds[i + 1]))
        i += 2

    processed_ranges = process_seed_range(input_seeds_ranges, almanac)
    return min(range_to_process.start for range_to_process in processed_ranges)
