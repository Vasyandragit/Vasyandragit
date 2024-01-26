def make_list(length, value=0):
    return [value] * length


def make_matrix(size, value=0):
    if type(size) is int:
        size = (size, size)
    return [make_list(size[0], value) for _ in range(size[1])]

print(make_matrix(3))