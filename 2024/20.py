from utils import read_str
from itertools import combinations

import networkx as nx


def read(fn):
    ss = read_str(fn)
    G = nx.grid_2d_graph(len(ss), len(ss[0]))
    for j, s in enumerate(ss):
        for i, c in enumerate(s):
            p = (i, j)
            if c == "#":
                G.remove_node(p)
            elif c == "S":
                start = p
    return G, start


def pzl(G, start, cheat_distance=2, min_saved=100):
    dist = nx.single_source_dijkstra_path_length(G, start)
    return sum([
        (d := abs(i1 - i2) + abs(j1 - j2)) <= cheat_distance and d2 - d1 - d >= min_saved
        for ((i1, j1), d1), ((i2, j2), d2) in combinations(dist.items(), 2)
    ])


t = read('20.tst')

assert pzl(*t, min_saved=20) == 5
assert pzl(*t, min_saved=64) == 1


d = read('20.dat')

print("day 20 puzzle 1 =", pzl(*d))
print("day 20 puzzle 2 =", pzl(*d, cheat_distance=20))
