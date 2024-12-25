from utils import read_str
import re


def read(fn):
    return [list(map(int, re.split(r": | ", l))) for l in read_str(fn)]


def is_true(test, numbers, two):
    last = numbers[-1]
    rest = numbers[:-1]

    if len(numbers) == 1:
        return last == test

    if test % last == 0 and is_true(test // last, rest, two):
        return True

    if test > last and is_true(test - last, rest, two):
        return True

    if two:
        test_str = str(test)
        last_str = str(last)
        if (test_str.endswith(last_str) and len(test_str) > len(last_str) and
                is_true(int(test_str[:-len(last_str)]), rest, two)):
            return True

    return False


def pzl(equations, two=False):
    res = 0
    for equation in equations:
        test = equation[0]
        numbers = equation[1:]
        if is_true(test, numbers, two):
            res += test
    return res


t = read('07.tst')

assert pzl(t) == 3749
assert pzl(t, True) == 11387

d = read('07.dat')

print("day 7 puzzle 1 =", pzl(d))
print("day 7 puzzle 2 =", pzl(d, True))
