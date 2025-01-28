N = int(input())

def num_square(n):
    if n != 0:
        return num_square(n // 10) + (n % 10) ** 2
    else:
        return 0

print(num_square(N))
