from utils import read_groups
from functools import cache

ts = set()
ds = list()


def read(fn):
    global ts, ds
    ts, ds = read_groups(fn)
    ts, ds = {t.strip() for t in ts[0].split(',')}, ds


@cache
def count(d: str, test):
    if not len(d):
        return 1
    return sum([c for t in ts if d.startswith(t) and (c := count(d[len(t):], test))])


def pzl(fn, test=False):
    return sum([fn(count(d, test)) for d in ds])


read('19.tst')

# test variable for valid caching
assert pzl(bool, test=True) == 6
assert pzl(int, test=True) == 16

read('19.dat')

print("day 19 puzzle 1 =", pzl(bool))
print("day 19 puzzle 2 =", pzl(int))
