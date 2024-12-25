import networkx as nx
from utils import read_str, cardinal_directions
dirs = cardinal_directions.values()


def pzl(fn, two=False):
    G = nx.DiGraph()

    for j, s in enumerate(read_str(fn)):
        for i, c in enumerate(s):
            if c == '#':
                continue
            z = i + j * 1j
            if c == "S":
                start = (z, 1)
            if c == "E":
                end = z
            for cd in dirs:
                G.add_node((z, cd))

    for z, cd in G.nodes:
        # к соседям
        if (z + cd, cd) in G.nodes:
            G.add_edge((z, cd), (z + cd, cd), w=1)
        # поворот внутри одной точки
        for rot in -1j, 1j:
            G.add_edge((z, cd), (z, cd * rot), w=1000)

    for cd in dirs:
        G.add_edge((end, cd), "E", w=0)

    if two:
        return len({
            z
            for path in nx.all_shortest_paths(G, start, "E", weight="w")
            for z, _ in path[:-1]
        })

    return nx.shortest_path_length(G, start, "E", weight="w")


assert pzl('16.tst') == 7036

print("day 16 puzzle 1 =", pzl('16.dat'))
print("day 16 puzzle 2 =", pzl('16.dat', two=True))
