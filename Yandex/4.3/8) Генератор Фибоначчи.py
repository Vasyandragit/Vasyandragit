def fibo(n):
    f1, f2 = 0, 1
    for _ in range(n):
        yield f1
        f1, f2 = f2, f1 + f2
        
        
print(*fibo(10))