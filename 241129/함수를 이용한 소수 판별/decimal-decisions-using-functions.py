def is_prime(n):
    if n == 1:
        return False
    
    for _ in range(2, n):
        if n % _ == 0:
            return False
    
    return True

a, b = map(int, input().split())

sum_ = 0

for _ in range(a, b + 1):
    if is_prime(_):
        sum_ += _

print(sum_)
