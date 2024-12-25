from functools import cache


@cache
def count(mark, blink):
    if blink == 0:
        return 1
    blink -= 1
    if mark == 0:
        return count(1, blink)
    mark_str = str(mark)
    quotient, remainder = divmod(len(mark_str), 2)
    if remainder == 0:
        return count(int(mark_str[:quotient]), blink) + count(int(mark_str[quotient:]), blink)
    return count(mark * 2024, blink)


def pzl(stones, blinks):
    return sum([count(stone, blinks) for stone in stones])


assert pzl([125, 17], 6) == 22

data = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]

print("day 11 puzzle 1 =", pzl(data, 25))
print("day 11 puzzle 2 =", pzl(data, 75))
