from utils import read_int
from collections import defaultdict

import numpy as np


def hsh(secret):
    for _ in range(2000):
        secret ^= secret << 6 & 0xFFFFFF
        secret ^= secret >> 5 & 0xFFFFFF
        secret ^= secret << 11 & 0xFFFFFF
        yield secret


def pzl1(nums):
    return sum(
        [list(hsh(x))[-1] for x in nums]
    )


def pzl2(nums):
    res = defaultdict(int)
    for x in nums:
        buyer = [s % 10 for s in hsh(x)]
        diffs = np.diff(buyer)
        seen = set()
        for i in range(1996):
            if (d := tuple(diffs[i: i + 4])) not in seen:
                seen.add(d)
                res[d] += buyer[i + 4]
    return max(res.values())


assert pzl1([1, 10, 100, 2024]) == 37327623
assert pzl2([1, 2, 3, 2024]) == 23


print("day 22 puzzle 1 =", pzl1(read_int('input')))
print("day 22 puzzle 2 =", pzl2(read_int('input')))
