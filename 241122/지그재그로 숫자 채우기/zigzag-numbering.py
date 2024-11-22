n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

value = 0

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            arr_2d[j][i] = value
            value += 1
        else:
            arr_2d[n - 1 - j][i] = value
            value += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=' ')
    print()
