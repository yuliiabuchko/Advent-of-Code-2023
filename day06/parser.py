"""Module parses and processes input"""
import dataclasses


@dataclasses.dataclass
class Game:
    """Input game"""
    time: int
    record_distance: int


def parser(input_path: str) -> list[Game]:
    """Function reads and parses input"""
    with open(input_path, 'r', encoding='utf-8') as input_file:
        times = list(map(int, input_file.readline().split(":")[1].split()))
        distances = list(map(int, input_file.readline().split(":")[1].split()))
        return [Game(t, d) for t, d in zip(times, distances)]
