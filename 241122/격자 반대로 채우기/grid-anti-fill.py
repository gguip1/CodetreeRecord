n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

value = 1

for i in range(n):
    for j in range(n):
        if (n - i - 1) % 2 != 0:
            arr_2d[n - j - 1][n - i - 1] = value
            value += 1
        else:
            arr_2d[j][n - i - 1] = value
            value += 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=' ')
    print()