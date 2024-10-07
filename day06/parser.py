class Game:
    def __init__(self, time: int, record_distance: int):
        self.time = time
        self.record_distance = record_distance


def parser(input_path: str) -> list[Game]:
    with open(input_path, 'r') as input_file:
        times = list(map(int, input_file.readline().split(":")[1].split()))
        distances = list(map(int, input_file.readline().split(":")[1].split()))
        return [Game(t, d) for t, d in zip(times, distances)]
