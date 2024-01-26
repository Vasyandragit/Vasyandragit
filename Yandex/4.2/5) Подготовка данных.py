def to_string(*seq, sep=' ', end='\n'):
    return sep.join(str(i) for i in seq) + end

print(to_string(1, 2, 3))