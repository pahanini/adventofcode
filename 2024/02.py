import numpy as np
from utils import read_str

valid = [-3, -2, -1, 1, 2, 3]


def read(fn):
    return [np.array(f.split(), dtype=int) for f in read_str(fn)]


def chk(a):
    dd = np.diff(a)
    x = dd.max()
    y = dd.min()
    return x * y > 0 and x in valid and y in valid


def pzl(aa, two=False):
    r = 0
    for a in aa:
        if chk(a):
            r += 1
        elif two:
            for i in range(len(a)):
                if chk(np.delete(a, i)):
                    r += 1
                    break

    return r


t = read('02.tst')

assert pzl(t) == 2
assert pzl(t, two=True) == 4

d = read('02.dat')

print("day 2 puzzle 1 =", pzl(d))
print("day 2 puzzle 2 =", pzl(d, two=True))
