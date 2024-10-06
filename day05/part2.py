from day05.parser import Almanac
from day05.part1 import process_seed


def part2(almanac: Almanac) -> int:
    seeds_ranges = []
    i = 0
    while i < len(almanac.seeds):
        seeds_ranges.append((almanac.seeds[i], almanac.seeds[i] + almanac.seeds[i + 1]))
        i += 2
    min_value = float("inf")
    for seed_range in seeds_ranges:
        for seed in range(seed_range[0], seed_range[1]):
            value = process_seed(seed, almanac)
            print(value)
            if value < min_value:
                min_value = value
    return min_value
