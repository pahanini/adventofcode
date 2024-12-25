from utils import read_str
from collections import defaultdict
from itertools import permutations


board = {}
antennas = defaultdict(list)


def read(fn):
    global board, antennas
    board = {i + 1j * j: c for i, s in enumerate(read_str(fn)) for j, c in enumerate(s)}
    antennas = defaultdict(list)
    for i, v in board.items():
        if v != ".":
            antennas[v].append(i)


def pzl1():
    return len({2 * a - b for antenna in antennas.values() for a, b in permutations(antenna, 2)} & board.keys())


def pzl2():
    antinodes = set()
    for antenna in antennas.values():
        for a, b in permutations(antenna, 2):
            c = b
            while c in board:
                antinodes.add(c)
                c += b - a
    return len(antinodes)


read('08.tst')

assert pzl1() == 14
assert pzl2() == 34


read('08.dat')

print("day 8 puzzle 1 =", pzl1())
print("day 8 puzzle 2 =", pzl2())

