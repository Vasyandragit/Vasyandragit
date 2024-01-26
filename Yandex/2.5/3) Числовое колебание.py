N, M, D = int(input()), int(input()), int(input())

for i in range(N, M + 1, D):
    print(i, end=' - ')
for j in range(M, N - 1, -D):
    print(j, end=' - ' if j != N else '\n')