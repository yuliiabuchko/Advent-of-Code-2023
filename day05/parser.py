class GameRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class GameEntry:
    def __init__(self, destination_start: int, source_start: int, range_length: int) -> None:
        self.source = GameRange(source_start, source_start + range_length)
        self.destination = GameRange(destination_start, destination_start + range_length)

    def calculate_destination_for_number(self, number: int) -> int:
        return self.destination.start + number - self.source.start

    def contains_number(self, number: int) -> bool:
        return self.source.start <= number < self.source.end


class GameMap:
    def __init__(self, source: str, destination: str) -> None:
        self.source = source
        self.destination = destination
        self.entries: list[GameEntry] = []

    def add_entries(self, destination_start: int, source_start: int, range_length: int) -> None:
        self.entries.append(GameEntry(destination_start, source_start, range_length))


class Almanac:
    def __init__(self, seeds: list[int]):
        self.seeds = seeds
        self.maps: list[GameMap] = []

    def add_map(self, game_map: GameMap) -> None:
        self.maps.append(game_map)


def parser(input_path: str) -> Almanac:
    with open(input_path, 'r') as input_file:
        seeds_str = input_file.readline()
        seeds = list(map(int, seeds_str.split(":")[1].split()))
        almanac = Almanac(seeds)
        input_file.readline()

        curr_map = None
        for line in input_file.readlines():
            if line.strip() == '':
                almanac.add_map(curr_map)
                curr_map = None
            elif line[0].isalpha():
                _from, _, _to = line.split()[0].split('-')
                curr_map = GameMap(_from, _to)
            else:
                destination_start, source_start, range_length = line.strip().split()
                curr_map.add_entries(int(destination_start), int(source_start), int(range_length))
        almanac.add_map(curr_map)
    return almanac
