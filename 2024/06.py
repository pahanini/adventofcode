from utils import read_str

walls = set()
start = 0
start_course = -1
board = dict()


def read(fn):
    global start, walls, board
    board = {i + 1j * j: v for i, l in enumerate(read_str(fn)) for j, v in enumerate(l)}
    start = next(w for w, x in board.items() if x == "^")
    walls = {w for w, x in board.items() if x == "#"}


def find_path():
    seen = set()
    cur = start
    course = start_course
    while cur in board:
        seen.add(cur)
        if cur + course in walls:
            course *= -1j
            continue
        cur += course
    return seen


def test_loop(candidate) -> bool:
    test_walls = walls | {candidate}
    cur = start
    seen = set()
    course = start_course
    while cur in board:
        if (cur, course) in seen:
            return True
        seen.add((cur, course))
        if cur + course in test_walls:
            course *= -1j
            continue
        cur += course

    return False


def pzl1(v):
    return len(v)


def pzl2(v):
    return sum(test_loop(w) for w in v)


read('06.tst')
path = find_path()

assert pzl1(path) == 41
assert pzl2(path) == 6


read('06.dat')
path = find_path()

print("day 6 puzzle 1 =", pzl1(path))
print("day 6 puzzle 2 =", pzl2(path))
