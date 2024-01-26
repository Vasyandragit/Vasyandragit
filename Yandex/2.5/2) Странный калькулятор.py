a, s, b = int(input()), input(), int(input())

if len(s) % 2 and ' ' in s:
    print(a * b)
elif len(s) % 2 == 0:
    if ' ' in s:
        print(a + b)
    else:
        print(a - b)
else:
    print(a // b)