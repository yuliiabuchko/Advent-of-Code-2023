def parser(input_path: str) -> list[str]:
    with open(input_path, 'r') as input_file:
        return input_file.readlines()
