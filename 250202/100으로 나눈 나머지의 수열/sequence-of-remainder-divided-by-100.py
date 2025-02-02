N = int(input())

def func(a, b, N):
    N -= 1
    
    if N == 0:
        return a
    
    return func(b, (a * b) % 100, N)

print(func(2, 4, N))