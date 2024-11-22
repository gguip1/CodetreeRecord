n, m = map(int, input().split())

position = [
    list(map(int, input().split()))
    for _ in range(m)    
]

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        for _ in position:
            if i + 1 == _[0] and j + 1 == _[1]:
                arr_2d[_[0] - 1][_[1] - 1] = _[0] * _[1]
        print(arr_2d[i][j], end=' ')
    print()
