import numpy as np


def pzl1(a):
    a.sort(axis=0)
    return np.sum(np.abs(np.diff(a, axis=1)))


def pzl2(a):
    c = np.apply_along_axis(lambda x: np.bincount(x, minlength=100000), 0, a)
    return sum(np.multiply(np.arange(100000), np.multiply(c[:, 0], c[:, 1])))


t = np.loadtxt('0.tst', dtype=int)

assert pzl1(t) == 11
assert pzl2(t) == 31

d = np.loadtxt('input', dtype=int)

print("day 1 puzzle 1 =", pzl1(d))
print("day 1 puzzle 2 =", pzl2(d))
