n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

position = [
    [] for _ in range(n + m - 1)
]

for i in range(n):
    for j in range(m):
        for _ in range(n + m - 1):
            if i + j == _:
                position[i+j].append([i, j])

value_ = 1

for value in position:
    for v in value:
        arr_2d[v[0]][v[1]] = value_
        value_ += 1

for i in range(n):
    for j in range(m):
        print(arr_2d[i][j], end=' ')
    print()
