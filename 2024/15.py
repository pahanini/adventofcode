from utils import read_groups

dirs = {"^": -1j, "v": 1j, "<": -1, ">": 1}


def pzl(fn, two=False):
    maze, moves = read_groups(fn)
    boxes = set()
    walls = set()

    k = 2 if two else 1
    for j, s in enumerate(maze):
        for i, c in enumerate(s):
            z = i*k + j*1j
            match c:
                case '#':
                    walls |= {z, z+1} if two else {z}
                case 'O':
                    boxes.add(z)
                case '@':
                    robot = z

    moves = [dirs[m] for m in "".join(moves)]

    i = 0
    for move in moves:
        to_move = set()
        i += 1
        to_check = [robot + move]
        while to_check:

            z = to_check.pop()
            if z in walls:
                break

            is_right = two and (left_z := z - 1) in boxes

            if z in boxes or is_right:
                to_move.add(left_z if is_right else z)
                to_check.append(z + move)

                if two and move.imag:
                    to_check.append((left_z if is_right else z + 1) + move)

        else:
            robot += move
            boxes -= to_move
            boxes |= {z + move for z in to_move}

    total = sum(boxes)
    return int(total.imag * 100 + total.real)


assert pzl('15.tst') == 10092
assert pzl('15.tst', two=True) == 9021

print("day 15 puzzle 1 =", pzl('15.dat'))
print("day 15 puzzle 2 =", pzl('15.dat', two=True))
