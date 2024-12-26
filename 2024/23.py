from utils import read_str
import networkx as nx


def cliques(fn):
    return list(nx.enumerate_all_cliques(nx.Graph([s.split('-') for s in read_str(fn)])))


def pzl1(cs):
    return len([c for c in cs if len(c) == 3 and any([x[0] == 't' for x in c])])


def pzl2(cs):
    return ",".join(sorted(list(cs)[-1]))


t = cliques('23.1.tst')
assert pzl1(t) == 7

t = cliques('23.2.tst')
assert pzl2(t) == "co,de,ka,ta"

d = cliques('input')

print("day 23 puzzle 1 =", pzl1(d))
print("day 23 puzzle 2 =", pzl2(d))
