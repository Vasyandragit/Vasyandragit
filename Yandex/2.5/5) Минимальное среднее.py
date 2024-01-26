N = int(input())

mi = 10 ** 10
for _ in range(N):
    co = su = 0
    while (n := input()) != 'end':
        su += int(n)
        co += 1
    mi = min(mi, su / co)
print(f'{mi:.2f}')