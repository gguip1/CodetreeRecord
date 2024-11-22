n, m = map(int, input().split())

position = [
    list(map(int, input().split()))
    for _ in range(m)
]

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for value in position:
    arr_2d[value[0] - 1][value[1] - 1] = 1

for i in range(n):
    for j in range(n):
        print(arr_2d[i][j], end=' ')
    print()
