n = int(input())
_ = []

for i in range(n):
    __ = []
    for j in range(n):
        __.append(0)
    _.append(__)


num = 1

for i in range(n, 0, -1):
    if n % 2 == 0:
        if i % n == 0 or (i % n) % 2 == 0:
            for j in range(n, 0, -1):
                _[j-1][i-1] = num
                num += 1
        else:
            for j in range(n):
                _[j][i - 1] = num
                num += 1
    else:
        if i % n == 0 or (i % n) % 2 != 0:
            for j in range(n, 0, -1):
                _[j-1][i-1] = num
                num += 1
        else:
            for j in range(n):
                _[j][i - 1] = num
                num += 1

for i in range(n):
    for j in range(n):
        print(_[i][j], end=' ')
    print()