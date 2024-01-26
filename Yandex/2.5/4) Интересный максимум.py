N, M = int(input()), int(input())

prev_num = int(input())
ma = -10 ** 10
for _ in range(N - 1):
    
    next_num = int(input())
    if abs(next_num - prev_num) < M:
        ma = max(next_num, ma)
    prev_num = next_num
print(ma)