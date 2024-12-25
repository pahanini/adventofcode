import re


def read_complex_board(filename: str, converter=lambda t: t) -> dict:
    return {i + j * 1j: converter(c) for j, s in enumerate(read_str(filename)) for i, c in enumerate(s)}


def read_int(filename: str) -> list:
    with open(filename) as file:
        lines = [int(line.strip()) for line in file]
    return lines


def read_re(filename: str, pattern) -> list:
    with open(filename) as file:
        lines = [re.search(pattern, line.strip()).groups() for line in file]
    return lines


def read_str(filename: str) -> list:
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines


def read_groups(filename: str, strip: bool = True) -> list:
    with open(filename) as file:
        data = file.read()
        if strip:
            data = data.strip()
    return [s.split('\n') for s in data.split('\n\n')]


def read_all(filename: str) -> str:
    with open(filename) as file:
        data = file.read().strip()
    return data
