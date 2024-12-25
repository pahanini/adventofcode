from utils import read_str
from copy import copy


class B:

    def __init__(self, idx, size):
        self.value = None if idx % 2 else int(idx // 2)
        self.size = int(size)


class FS:

    def __init__(self):
        self.blocks = []

    def read(self, fn):
        self.blocks = sum([[B(idx, size) for _ in range(int(size))] for idx, size in enumerate(read_str(fn)[0])], [])
        return self

    def copy(self):
        c = FS()
        c.blocks = [copy(b) for b in self.blocks]
        return c


def read(fn):
    return sum([[B(idx, size) for _ in range(int(size))] for idx, size in enumerate(read_str(fn)[0])], [])


def calc(fs: list[B]):
    return sum([i * b.value for i, b in enumerate(fs) if b.value is not None])


def pzl1(fs: FS):
    left = 0
    blocks = fs.blocks
    right = len(blocks) - 1
    while right > left:
        if blocks[right].value is None:
            right -= 1
            continue
        if blocks[left].value is not None:
            left += 1
            continue
        blocks[right], blocks[left] = blocks[left], blocks[right]
    return calc(blocks)


def pzl2(fs: FS):
    blocks = fs.blocks
    right = len(blocks) - 1

    while right > 0:
        right -= blocks[right].size - 1
        file_size = blocks[right].size
        file_value = blocks[right].value

        if blocks[right].value is not None:

            left = 0
            while (blocks[left].size < file_size or blocks[left].value is not None) and left < right:
                left += blocks[left].size

            if left < right:
                diff = blocks[left].size - file_size
                for i in range(file_size):
                    blocks[left + i].size = file_size
                    blocks[left + i].value = file_value
                    blocks[right + i].size = file_size
                    blocks[right + i].value = None
                for j in range(diff):
                    blocks[left + 1 + i + j].size = diff
                    blocks[left + 1 + i + j].value = None

        right -= 1

    return calc(blocks)


t = FS().read('09.tst')

assert pzl1(t.copy()) == 1928
assert pzl2(t.copy()) == 2858


d = FS().read('09.dat')

print("day 9 puzzle 1 =", pzl1(d.copy()))
print("day 8 puzzle 2 =", pzl2(d.copy()))

