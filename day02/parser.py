class GameEntry:
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0

    def set_red(self, red: int):
        self.red = red

    def set_green(self, green: int):
        self.green = green

    def set_blue(self, blue: int):
        self.blue = blue


class Game:
    def __init__(self, num: int):
        self.id = num
        self.entries = []

    def add_entry(self, entry: GameEntry):
        self.entries.append(entry)


def parser(path: str) -> list[Game]:
    res = []
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line[len("Game "):]
            game_num_str, game_entries_str = line.split(":")
            game = Game(int(game_num_str))
            entries = game_entries_str.split(";")
            for entry_str in entries:
                entry = GameEntry()
                by_colors = entry_str.split(",")
                for by_color in by_colors:
                    by_color = by_color.strip()
                    num_str, color = by_color.split()
                    match color:
                        case "green":
                            entry.set_green(int(num_str))
                        case "red":
                            entry.set_red(int(num_str))
                        case "blue":
                            entry.set_blue(int(num_str))
                game.add_entry(entry)
            res.append(game)
    return res
