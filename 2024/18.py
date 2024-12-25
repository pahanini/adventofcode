from utils import read_str
import networkx as nx


def pzl(fn, size=70, last=1023):
    bad = [tuple(map(int, s.split(','))) for s in read_str(fn)]
    G = nx.grid_2d_graph(size + 1, size + 1)
    for i, b in enumerate(bad):
        G.remove_node(b)
        if i == last:
            one = nx.shortest_path_length(G, (0, 0), (size, size))
        elif not nx.has_path(G, (0, 0), (size, size)):
            two = f"{b[0]},{b[1]}"
            break
    return one, two


one, two = pzl('18.tst', size=6, last=11)

assert one == 22
assert two == '6,1'

one, two = pzl('18.dat')

print("day 18 puzzle 1 =", one)
print("day 18 puzzle 2 =", two)
