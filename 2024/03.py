from utils import read_all
import re

r = re.compile(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))")


def pzl(s, two=False) -> int:
    do = True
    res = 0
    for m, x, y in r.findall(s):
        if m == "don't()":
            do = False
        elif m == "do()":
            do = True
        else:
            if do or not two:
                res += int(x) * int(y)
    return res


t = read_all('03-1.tst')
assert pzl(t) == 161

t = read_all('03-2.tst')
assert pzl(t, two=True) == 48

d = read_all('03.dat')

print("day 3 puzzle 1 =", pzl(d))
print("day 2 puzzle 2 =", pzl(d, two=True))
