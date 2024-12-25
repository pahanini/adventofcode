def apply(f, a, b):
    return tuple(map(f, zip(a, b)))


def op(t, a, b):
    return tuple(map(t, a, b))

