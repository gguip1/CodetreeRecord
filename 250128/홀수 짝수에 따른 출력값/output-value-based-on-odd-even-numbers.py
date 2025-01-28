N = int(input())

def even(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + even(n - 1)
    else:
        return even(n - 1)

def odd(n):
    if n <= 0:
        return 0
    if n % 2 == 1:
        return n + odd(n - 1)
    else:
        return odd(n - 1)

if N % 2 == 0:
    print(even(N))
else:
    print(odd(N))
