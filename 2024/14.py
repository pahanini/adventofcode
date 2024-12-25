from utils import read_str
from math import prod
import re


def read(fn):
    return [list(map(int, re.findall(r'-?\d+', g))) for g in read_str(fn)]


def pzl1(robots, w=101, h=103, steps=100):
    q = [0] * 4
    for px, py, vx, vy in robots:
        px = (px + vx * steps) % w
        py = (py + vy * steps) % h
        hw = (w - 1) // 2
        hh = (h - 1) // 2
        if px != hw and py != hh:
            q[(px > hw) + 2 * (py > hh)] += 1
    return prod(q)


def pzl2(robots, w=101, h=103):
    min_sf = float("inf")
    best = None
    q = [0] * 4
    for second in range(h*w):
        sf = pzl1(robots, w, h, steps=second)
        if sf < min_sf:
            min_sf = sf
            best = second
    return best


t = read('14.tst')
print(t)

assert pzl1(t, w=11, h=7) == 12

d = read('14.dat')

print("day 14 puzzle 1 =", pzl1(d))
print("day 14 puzzle 2 =", pzl2(d))
