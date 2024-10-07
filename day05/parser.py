"""Module parses and processes input"""
import dataclasses


@dataclasses.dataclass
class GameRange:
    """Range from start (including) to end (not including)"""
    start: int
    end: int


class GameEntry:
    """Single game entry with source and destination ranges"""

    def __init__(self, destination_start: int, source_start: int, range_length: int) -> None:
        self.source = GameRange(source_start, source_start + range_length)
        self.destination = GameRange(destination_start, destination_start + range_length)

    def calculate_destination_for_number(self, number: int) -> int:
        """Calculate destination for number"""
        return self.destination.start + number - self.source.start

    def contains_number(self, number: int) -> bool:
        """Check if number is within source range"""
        return self.source.start <= number < self.source.end


@dataclasses.dataclass
class GameMap:
    """Map from source to destination with entries"""
    source: str
    destination: str
    entries: list[GameEntry]


@dataclasses.dataclass
class Almanac:
    """Input almanac"""
    seeds: list[int]
    maps: list[GameMap]



def parser(input_path: str) -> Almanac:
    """Function reads and parses input"""
    with open(input_path, 'r', encoding='utf-8') as input_file:
        seeds_str = input_file.readline()
        seeds = list(map(int, seeds_str.split(":")[1].split()))
        almanac = Almanac(seeds, [])
        input_file.readline()

        curr_map = None
        for line in input_file.readlines():
            if line.strip() == '':
                assert curr_map is not None
                almanac.maps.append(curr_map)
                curr_map = None
            elif line[0].isalpha():
                _from, _, _to = line.split()[0].split('-')
                curr_map = GameMap(_from, _to, [])
            else:
                destination_start, source_start, range_length = map(int, line.strip().split())
                assert curr_map is not None
                curr_map.entries.append(GameEntry(destination_start, source_start, range_length))
        assert curr_map is not None
        almanac.maps.append(curr_map)
    return almanac
