"""Module parses and processes input"""
import dataclasses


class GameEntry:
    """Single game set entry"""
    def __init__(self) -> None:
        self.red = 0
        self.green = 0
        self.blue = 0

    def set_red(self, red: int) -> None:
        """Set red balls count"""
        self.red = red

    def set_green(self, green: int) -> None:
        """Set green balls count"""
        self.green = green

    def set_blue(self, blue: int) -> None:
        """Set blue balls count"""
        self.blue = blue


@dataclasses.dataclass
class Game:
    """Game with entries sets"""
    id: int
    entries: list[GameEntry]


def parser(path: str) -> list[Game]:
    """Function reads and parses input"""
    res = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            line = line[len("Game "):]
            game_num_str, game_entries_str = line.split(":")
            entries_str = game_entries_str.split(";")
            entries = []
            for entry_str in entries_str:
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
                entries.append(entry)
            res.append(Game(int(game_num_str), entries))
    return res
