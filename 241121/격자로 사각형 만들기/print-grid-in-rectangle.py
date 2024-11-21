n = int(input())

_ = []

for i in range(n):
    __ = []
    for j in range(n):
        if j == 0 or i == 0:
            __.append(1)
        else:
            __.append(0)
    _.append(__)

for i in range(1, n):
    for j in range(1, n):
        _[i][j] = _[i-1][j] + _[i][j-1] + _[i-1][j-1]

for i in range(n):
    for j in range(n):
        print(_[i][j], end=' ')
    print()