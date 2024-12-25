from utils import read_str
from itertools import pairwise
from functools import cache
import networkx as nx
from utils import cardinal_directions

A = 'A'
U = '^'
D = 'v'
L = '<'
R = '>'

num_kbd = {0: '7', 1: '8', 2: '9', 0 + 1j: '4', 1 + 1j: '5', 2 + 1j: '6', 0 + 2j: '1',
           1 + 2j: '2', 2 + 2j: '3', 1 + 3j: '0', 2 + 3j: A}
dir_kbd = {1: U, 2: A, 1j: L, 1 + 1j: D, 2 + 1j: R}
dirs = {1j: D, -1j: U, 1: R, -1: L}


def make_paths(kbd):
    zs = kbd.keys()
    G = nx.DiGraph([(z, z + cd) for z in zs for cd in cardinal_directions.values() if z + cd in zs])
    res = {}
    for start, ends in nx.all_pairs_all_shortest_paths(G):
        for end, paths in ends.items():
            res[(kbd[start], kbd[end])] = list()
            for path in paths:
                res[(kbd[start], kbd[end])].append("".join([dirs[e-s] for s, e in pairwise(path)]))
    return res


num_paths = make_paths(num_kbd)
dir_paths = make_paths(dir_kbd)


@cache
def shortest(input_seq, robot=0, last_robot=2):
    if robot == last_robot + 1:
        return len(input_seq)
    paths = dir_paths if robot else num_paths
    return sum(
        min(
            shortest(seq + A, robot + 1, last_robot)
            for seq in paths[start, end]
        )
        for start, end in pairwise(A + input_seq)
    )


def pzl(fn, last_robot):
    return sum([int(s[:-1]) * shortest(s, last_robot=last_robot) for s in read_str(fn)])


print("day 21 puzzle 1 =", pzl('input', 2))
print("day 21 puzzle 2 =", pzl('input', 25))
