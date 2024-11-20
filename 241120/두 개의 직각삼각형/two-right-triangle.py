n = int(input())

for i in range(n):
    result = '*' * (n - i) + ' ' * i + ' ' * i + '*' * (n - i)
    print(result)
