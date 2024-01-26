a, b, c = int(input()), int(input()), int(input())
print(f'({a} ^ {b}) mod ({a} + {c}) = {(a ** b) % (a + b)}')