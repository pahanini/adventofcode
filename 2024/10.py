from utils import read_complex_board, cardinal_directions
from itertools import product
import networkx as nx

board = dict()
heads = list()
ends = list()
G = None


def read(fn):
    global G, board, heads, ends

    board = read_complex_board(fn, lambda t: int(t))
    heads = [k for k, v in board.items() if v == 0]
    ends = [k for k, v in board.items() if v == 9]

    G = nx.DiGraph()
    for current, value in board.items():
        for direction in cardinal_directions.values():
            neighbour = current + direction
            if neighbour in board and board[neighbour] - value == 1:
                G.add_edge(current, neighbour)


def pzl1():
    return sum([nx.has_path(G, head, end) for head, end in product(heads, ends)])


def pzl2():
    return sum([len(list(nx.all_simple_paths(G, head, end))) for head, end in product(heads, ends)])


read('10.tst')

assert pzl1() == 36
assert pzl2() == 81

read('10.dat')

print("day 10 puzzle 1 =", pzl1())
print("day 10 puzzle 2 =", pzl2())
