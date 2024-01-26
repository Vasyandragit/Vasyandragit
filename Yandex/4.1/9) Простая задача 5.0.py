def is_prime(num):
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0 and i != 1:
            return False
    else:
        return True
    
print(is_prime(79701))