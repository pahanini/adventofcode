from utils import read_all
import re

A = 0
B = 1
C = 2


def read(fn):
    a, b, c, *code = map(int, re.findall(r"\d+", read_all(fn)))
    return [a, b, c], code


def run(reg, code) -> list[int]:
    result = []
    while reg[A] > 0:
        result.append(iteration(reg, code))
    return result


def iteration(reg, code):
    """
    Выполняет итерацию с учетом того что в конце всегда out, jnz
    """
    ptr = 0
    while True:
        ins = code[ptr]
        op = code[ptr + 1]
        combo = [0, 1, 2, 3, reg[A], reg[B], reg[C], None][op]
        match ins:
            case 0: reg[A] >>= combo            # adv
            case 1: reg[B] ^= op                # bxl
            case 2: reg[B] = combo % 8          # bst
            case 3: pass                        # jnz
            case 4: reg[B] ^= reg[C]            # bxc
            case 5: return combo % 8            # out
            case 6: reg[B] = reg[A] >> combo    # bdv
            case 7: reg[C] = reg[A] >> combo    # cdv
        ptr += 2


def find(target, code, init):
    if not target:
        return init

    for t in range(0, 8):
        a = init << 3 | t
        output = iteration([a, 0, 0], code)
        if target[-1] != output:
            continue

        res = find(target[:-1], code, a)
        if res is not None:
            return res


def pzl1(output):
    return ",".join(map(str, output))


def pzl2(output):
    return find(output, output, 0)


assert pzl1(run(*read('17.tst'))) == "4,6,3,5,6,3,5,2,1,0"
assert pzl2([0, 3, 5, 4, 3, 0]) == 117440

reg, code = read('17.dat')

print("day 17 puzzle 1 =", pzl1(run(reg, code)))
print("day 17 puzzle 2 =", pzl2(code))
