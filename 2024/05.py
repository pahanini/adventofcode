from utils import read_groups
import networkx as nx


def pzl(nn, pp, two=False) -> int:
    r = 0
    I = []
    for p in pp:
        G = nx.DiGraph()
        for a, b in nn:
            if a in p and b in p:
                G.add_edge(a, b)
        for a, b in zip(p[:-1], p[1:]):
            if not nx.has_path(G, a, b):
                I.append(G)
                break
        else:
            r += p[len(p) // 2]
    if two:
        r = 0
        for G in I:
            p = list(nx.topological_sort(G))
            r += p[len(p) // 2]

    return r


def read(fn):
    nn, pp = read_groups(fn)
    return [list(map(int, n.split("|"))) for n in nn], [list(map(int, p.split(','))) for p in pp]


t = read('05.tst')


assert pzl(*t) == 143
assert pzl(*t, two=True) == 123


d = read('05.dat')

print("day 4 puzzle 1 =", pzl(*d))
print("day 4 puzzle 2 =", pzl(*d, two=True))
