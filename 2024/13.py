from utils import read_all
import re
import z3


def read(fn):
    return [list(map(int, re.findall(r'\d+', g))) for g in read_all(fn).split('\n\n')]


def pzl(groups, offset=0):
    res = 0
    for ax, ay, bx, by, px, py in groups:
        px += offset
        py += offset
        a = z3.Int("a")
        b = z3.Int("b")
        s = z3.Solver()
        s.add(a * ax + b * bx == px)
        s.add(a * ay + b * by == py)
        s.add(a >= 0)
        s.add(b >= 0)
        if s.check() == z3.sat:
            m = s.model()
            res += 3 * m[a].as_long() + m[b].as_long()
    return res


t = read('13.tst')

assert pzl(t) == 480

d = read('13.dat')

print("day 13 puzzle 1 =", pzl(d))
print("day 13 puzzle 2 =", pzl(d, offset=10000000000000))
