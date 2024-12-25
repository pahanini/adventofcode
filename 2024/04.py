from utils import read_str
from itertools import product

dirs = {i + 1j * j for i, j in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}
diag = {i + 1j * j for i, j in set(product((-1, 1), (-1, 1))) - {(0, 0)}}

word = ['X', 'M', 'A', 'S']
center = 'A'
corners = ['M', 'S']


def pzl1(a) -> int:
    return sum(
        [a[k+d*i] for i in range(4) if k+d*i in a] == word
        for k in list(a.keys())
        for d in dirs
    )


def pzl2(a) -> int:
    r = 0
    for k, v in a.items():
        if v != center:
            continue
        w = [a[k+d] for d in diag if k+d in a]
        if w.count(corners[0]) == w.count(corners[1]) == 2 and w[0] != w[3]:
            r += 1
    return r


def read(fn):
    return {i + 1j*j: c for i, s in enumerate(read_str(fn)) for j, c in enumerate(s)}


t = read('04-1.tst')
assert pzl1(t) == 18

t = read('04-21.tst')
assert pzl2(t) == 9

d = read('04.dat')

print("day 4 puzzle 1 =", pzl1(d))
print("day 4 puzzle 2 =", pzl2(d))
