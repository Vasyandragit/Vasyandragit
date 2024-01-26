def gcd(*seq):
    def gcd_of_2nums(a, b):
        while b:
            a, b = b, a % b
        return a
    a = 0
    for b in seq:
        a = gcd_of_2nums(a, b)
    return a

print(gcd(36, 48, 72, 156, 100500))