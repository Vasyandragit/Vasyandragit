def recursive_sum(*seq):
    if not seq:
        return 0
    return seq[0] + recursive_sum(*seq[1:])