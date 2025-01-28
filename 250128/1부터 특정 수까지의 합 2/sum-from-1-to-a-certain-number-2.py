N = int(input())

def sum_(n):
    if n == 1:
        return 1
    return sum_(n - 1) + n

print(sum_(N))
