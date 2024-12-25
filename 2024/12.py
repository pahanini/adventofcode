from utils import read_complex_board, cardinal_directions
import networkx as nx


def read(fn):
    board = read_complex_board(fn)
    G = nx.Graph((a, b) for a in board for cd in cardinal_directions.values() if board[a] == board.get(b := a + cd))
    G.add_nodes_from(board)
    return G


def pzl1(G):
    res = 0
    for cmp in nx.connected_components(G):
        fence = {(n, cd) for cd in cardinal_directions.values() for n in cmp if n + cd not in cmp}
        res += len(cmp) * len(fence)
    return res


def pzl2(G):
    res = 0
    for cmp in nx.connected_components(G):
        fence = {(n, cd) for cd in cardinal_directions.values() for n in cmp if n + cd not in cmp}
        res += len(cmp) * sum((n + cd * 1j, cd) not in fence for (n, cd) in fence)
    return res


t = read('12.tst')

assert pzl1(t) == 140
assert pzl2(t) == 80

d = read('12.dat')

print("day 12 puzzle 1 =", pzl1(d))
print("day 11 puzzle 2 =", pzl2(d))
