def recursive_digit_sum(num):
    if not num:
        return 0
    return int(str(num)[0]) + recursive_digit_sum(str(num)[1:])

print(recursive_digit_sum(123))