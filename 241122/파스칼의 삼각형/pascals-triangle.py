n = int(input())

arr_2d = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(i + 1):
        if i != 0 and j != 0 and j != i:
            arr_2d[i][j] = arr_2d[i - 1][j - 1] + arr_2d[i - 1][j]
        print(arr_2d[i][j], end=' ')
    print()
